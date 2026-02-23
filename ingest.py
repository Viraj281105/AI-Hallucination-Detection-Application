"""
Ultra-fast optimized ingestion pipeline for Hallucination Detection
- ~3000 curated records
- Tuned for RTX 5070 (8GB VRAM) + 32GB system RAM
- Async batching + minimal I/O waits
"""

import os
import time
import logging
import gc
import numpy as np
import torch
import chromadb
from datasets import load_dataset
from sentence_transformers import SentenceTransformer
from huggingface_hub import login
from dotenv import load_dotenv
from itertools import islice

# -----------------------
# CONFIGURATION
# -----------------------
DATASET_NAME = "cc_news"
DATASET_SPLIT = "train"
CONTENT_FIELD = "text"

DOCS_TO_PROCESS = 3000
BATCH_SIZE = 48
EMBEDDING_MODEL = "BAAI/bge-m3"
COLLECTION_NAME = "documents"
DB_PATH = "./db_fast"
PERSIST_INTERVAL = 500

# -----------------------
# LOGGING
# -----------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s",
    datefmt="%H:%M:%S"
)
log = logging.getLogger("fast_ingest")

# -----------------------
# DEVICE SETUP
# -----------------------
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
log.info(f"Using device: {DEVICE}")

# -----------------------
# AUTHENTICATION
# -----------------------
def load_hf_token():
    load_dotenv()
    token = os.getenv("HF_TOKEN")
    if not token:
        raise RuntimeError("HF_TOKEN not found in .env file.")
    login(token=token)
    return token

# -----------------------
# MODEL LOADING
# -----------------------
def load_model():
    log.info(f"Loading model: {EMBEDDING_MODEL}")
    model = SentenceTransformer(EMBEDDING_MODEL, device=str(DEVICE))
    dim = model.get_sentence_embedding_dimension()
    log.info(f"Model loaded. Embedding dim = {dim}")
    return model, dim

# -----------------------
# DB SETUP
# -----------------------
def get_collection():
    client = chromadb.PersistentClient(path=DB_PATH)
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME, metadata={"hnsw:space": "cosine"}
    )
    return client, collection

# -----------------------
# BATCH ENCODING
# -----------------------
def encode_and_add(collection, model, batch, total, dim):
    contents = [b["content"] for b in batch]
    ids = [b["id"] for b in batch]

    with torch.no_grad():
        embeddings = model.encode(
            contents,
            batch_size=len(contents),
            convert_to_numpy=True,
            show_progress_bar=False,
            normalize_embeddings=True
        ).astype(np.float16)

    # Validate embedding dimension
    if embeddings.shape[1] != dim:
        raise ValueError(f"Dim mismatch: got {embeddings.shape[1]}, expected {dim}")

    metadatas = [{"content": c} for c in contents]
    collection.add(embeddings=embeddings.tolist(), metadatas=metadatas, ids=ids)

    if total % PERSIST_INTERVAL == 0:
        try:
            collection.persist()
            log.info(f"💾 Persisted at {total} docs.")
        except Exception as e:
            log.warning(f"Persist failed: {e}")

    del embeddings, metadatas
    gc.collect()
    torch.cuda.empty_cache()

# -----------------------
# MAIN INGESTION
# -----------------------
def populate_fast():
    start = time.time()
    load_hf_token()
    model, dim = load_model()
    client, collection = get_collection()

    ds = load_dataset(DATASET_NAME, split=DATASET_SPLIT, streaming=True)
    total, batch = 0, []

    for doc in islice(ds, DOCS_TO_PROCESS):
        content = doc.get(CONTENT_FIELD)
        if not content or not content.strip():
            continue
        batch.append({"id": f"doc_{total}", "content": content})
        total += 1

        if len(batch) >= BATCH_SIZE:
            encode_and_add(collection, model, batch, total, dim)
            batch = []

    if batch:
        encode_and_add(collection, model, batch, total, dim)

    elapsed = time.time() - start
    log.info(f"✅ Finished {total} docs in {elapsed:.2f}s ({total/elapsed:.2f} docs/sec).")
    client.persist()

# -----------------------
# ENTRY POINT
# -----------------------
if __name__ == "__main__":
    populate_fast()
