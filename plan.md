# 🚀 AI Verifier Project Plan

This document tracks the high-level phases and weekly goals for the AI Verifier project.
Active, granular tasks are tracked in this repo's **GitHub Issues** tab.

---

## 🏛️ Phase 1: The Core Engine (Weeks 1-3)
**Goal:** A live, deployed, "headless" API.

* **[Week 1 Sprint: Setup & Ingestion]**
    * [X] Repo Setup (`git`, `.gitignore`, `LICENSE`)
    * [X] Documentation (`README.md`, `PLAN.md`, `CONTRIBUTING.md`)
    * [ ] `requirements.txt` & Python `venv` setup
    * [ ] Create GitHub Issues for Week 1
    * [ ] Build `ingest.py`
    * [ ] Load BGE Embedding Model (`BAAI/bge-large-en-v1.5`)
    * [ ] Load `cc_news` dataset
    * [ ] Implement ChromaDB storage
    * **Milestone:** A populated `/db` folder.

* **[Week 2 Sprint: The "Headless" API]**
    * [ ] Create GitHub Issues for Week 2
    * [ ] Build `main.py` with FastAPI
    * [ ] Load both BGE and NLI (RoBERTa) models on startup
    * [ ] Create Pydantic schemas (`VerifyRequest`, `VerifyResponse`)
    * [ ] Implement the core `verify_claim` logic
    * **Milestone:** A locally testable API via Insomnia/Postman.

* **[Week 3 Sprint: Docker & Deployment]**
    * [ ] Create GitHub Issues for Week 3
    * [ ] Write `test_main.py` with `pytest`
    * [ ] Create `Dockerfile` for the API
    * [ ] Create `.github/workflows/ci.yml` to run `pytest`
    * [ ] Deploy to Render
    * **Milestone:** A live, public API URL.

---

## 🎨 Phase 2: The Full-Stack Application (Weeks 4-5)
**Goal:** A modern web UI that anyone can use.

* **[Week 4 Sprint: Frontend UI]**
    * [ ] Create GitHub Issues for Week 4
    * [ ] Scaffold SvelteKit/React app in `/frontend`
    * [ ] Build main page UI (textbox, button, result card)
    * [ ] Write frontend `fetch` logic to call Render API
    * [ ] Deploy `/frontend` to Vercel
    * **Milestone:** A live, public website that can verify claims.

* **[Week 5 Sprint: The "Dual-Judge" (Mistral)]**
    * [ ] Create GitHub Issues for Week 5
    * [ ] Research Mistral 7B 4-bit quantization
    * [ ] Implement "accurate_judge" function in `main.py`
    * [ ] Create prompt template for Mistral NLI
    * [ ] Update `/verify` endpoint to accept a "judge_mode" parameter
    * [ ] Add "Judge Mode" dropdown to the frontend UI
    * **Milestone:** A user-selectable "fast" vs. "accurate" mode.

---

## ✨ Phase 3: Polish & "Wow" Features (Weeks 6-7)
**Goal:** A "product-ready" application.

* **[Week 6 Sprint: Evidence & History]**
    * [ ] Create GitHub Issues for Week 6
    * [ ] Refactor `verify_claim` to return the specific `evidence_snippet`
    * [ ] Update frontend to highlight the snippet
    * [ ] Add `sqlite3` DB to FastAPI for logging requests
    * [ ] Create `/history` endpoint and page
    * **Milestone:** App has a "memory" and shows specific evidence.

* **[Week 7 Sprint: Live Web Search]**
    * [ ] Create GitHub Issues for Week 7
    * [ ] Add `duckduckgo_search` library
    * [ ] Implement `search_web` function
    * [ ] Update `verify_claim` to fall back to web search on low-similarity
    * [ ] Update API response to show "Verified (via Web Search)"
    * **Milestone:** App can verify claims about current events.

---

## 🚀 Phase 4: Documentation & Launch (Week 8)
**Goal:** A portfolio-ready project.

* **[Week 8 Sprint: Launch Week]**
    * [ ] Create GitHub Issues for Week 8
    * [ ] Create a final Architecture Diagram (e.g., with Excalidraw)
    * [ ] Create a video/GIF demo of the app
    * [ ] Finalize `README.md` with the GIF, live URLs, and diagram
    * [ ] Set up `MkDocs` in a `/docs` folder for the User Guide & API Docs
    * [ ] Deploy documentation site to Vercel/GitHub Pages
    * **Milestone:** Post the project on LinkedIn/GitHub!
