# 🤖 AI Hallucination Detection Application

A full-stack application to detect and verify AI-generated text against a trusted knowledge base. This system uses a dual-judge (Retriever + NLI) architecture to provide fast, accurate, and explainable fact-checking.

This project is built as a complete, production-ready system, including a REST API, a web-based frontend, and a CI/CD pipeline.

![](httpsReadMe-Hero)

---

## ✨ Features

* **REST API:** A "headless" FastAPI backend that can be integrated into any application.
* **Vector Knowledge Base:** Uses **ChromaDB** for a 100% local, persistent vector database.
* **High-Accuracy Verification:** Implements a "Retriever-Judge" workflow:
    1.  **Retriever:** `BAAI/bge-large-en-v1.5` (a top-tier model) finds the most relevant evidence from the knowledge base.
    2.  **Judge:** `ynie/roberta-large-snli...` (a specialized NLI model) checks if the evidence **Contradicts** or **Entails** (supports) the claim.
* **Dockerized & Deployable:** The entire backend is containerized with Docker for seamless deployment on services like **Render**.
* **(WIP) Dual-Judge System:** Will allow users to select between a `fast` judge (RoBERTa) or an `accurate` judge (Mistral 7B) for a speed-vs-accuracy trade-off.
* **(WIP) Live Web Search:** Can (optionally) fall back to a live web search if the local knowledge base has no relevant information.
* **(WIP) Full-Stack UI:** A clean **SvelteKit/React** frontend deployed on **Vercel** that provides a simple, user-friendly interface.

---

## 🛠️ Tech Stack & Architecture

This project is built using a modern, decoupled (frontend/backend) architecture.

**Backend (API):**
* **Framework:** FastAPI (Python)
* **AI Models:**
    * `sentence-transformers` (for BGE-large)
    * `transformers` (for RoBERTa-large-NLI)
* **Database:** ChromaDB (Local Vector DB)
* **Testing:** `pytest`
* **Deployment:** Docker, Render

**Frontend (UI):**
* **Framework:** SvelteKit / React (VITE)
* **Styling:** Tailwind CSS
* **Deployment:** Vercel

**DevOps:**
* **CI/CD:** GitHub Actions (for automated testing)
* **Code:** Git & GitHub
* **Planning:** GitHub Issues & `PLAN.md`

---

## 🚀 How to Run Locally

### 1. Setup
1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/AI-Hallucination-Detection-Application.git](https://github.com/YOUR_USERNAME/AI-Hallucination-Detection-Application.git)
    cd AI-Hallucination-Detection-Application
    ```
2.  **Create a Python Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    .\venv\Scripts\activate   # On Windows
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Add Hugging Face Token:**
    * Create a file named `.env` in the project root.
    * Add your [Hugging Face token](https://huggingface.co/settings/tokens) to it:
        ```
        HF_TOKEN='hf_YOUR_TOKEN_HERE'
        ```

### 2. Build the Knowledge Base (One-Time Step)
This script will download the `cc_news` dataset, create embeddings, and build your local vector database in a `/db` folder. This will take several minutes.

```bash
python ingest.py
````

### 3\. Run the Backend API

```bash
uvicorn main:app --reload
```

Your API is now running at `http://127.0.0.1:8000`.
You can see the automatic API documentation at `http://127.0.0.1:8000/docs`.

### 4\. (Coming Soon) Run the Frontend

```bash
cd frontend
npm install
npm run dev
```

-----

## 🗺️ Project Roadmap

This project is being built in phases. The complete breakdown and weekly sprint plan are tracked in our `PLAN.md` file.

## 🤝 Contributing

This is a solo portfolio project, but it follows a professional Git workflow. See `CONTRIBUTING.md` for details on the branching strategy and commit conventions.

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

````
