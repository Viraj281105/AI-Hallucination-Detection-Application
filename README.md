Perfect. Let's get this done. A well-documented project is 90% of the way to being a great portfolio piece.

We'll create/update the three essential documentation files that should live in your repository:

1.  **`README.md`**: Your "store front." This is for recruiters and future-you.
2.  **`PLAN.md`**: Your internal "master plan." This keeps you organized.
3.  **`CONTRIBUTING.md`**: Your "professional touch." This shows you know how to work in a team.

Here is the detailed content for each.

-----

### 1\. The `README.md` File

This is your project's "store front." It's the most important file. Open your existing `README.md` and replace its content with this.

````markdown
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

---

### 2. The `PLAN.md` File

Create a new file named `PLAN.md` in your root folder. This is your internal "master plan" that you decided on instead of Notion.

```markdown
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
````

-----

### 3\. The `CONTRIBUTING.md` File

Create a new file named `CONTRIBUTING.md` in your root folder. This shows you think about collaboration.

````markdown
# How to Contribute

This is a solo-developer portfolio project, but it follows a professional Git workflow for all new features and fixes.

## 1. Setting Up
1.  Fork and clone the repository.
2.  Follow the setup steps in `README.md` to create your `venv` and install dependencies.
3.  Run `python ingest.py` to build your local database.
4.  Run `pytest` to ensure all tests pass.

## 2. Branching & Commits
This project follows a simple `develop` -> `feature` branch workflow.

* **`main`**: This branch is for stable, deployed code. Do not commit here directly.
* **`develop`**: This is the main integration branch for new features. All Pull Requests should target `develop`.
* **`feature/...` or `fix/...`**: All work must be done on a feature or fix branch.

**Workflow:**
1.  Pull the latest from `develop`:
    ```bash
    git checkout develop
    git pull
    ```
2.  Create your new feature branch (referencing a GitHub Issue # if possible):
    ```bash
    git checkout -b feature/1-my-new-feature
    ```
3.  Write your code and **make sure `pytest` passes** before pushing.

## 3. Commit Message Convention
Please use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for your commit messages. This helps keep the project history clean.

* `feat:` A new feature (e.g., `feat: Add Mistral judge logic`)
* `fix:` A bug fix (e.g., `fix: Correct NLI probability indexing`)
* `docs:` Documentation changes (e.g., `docs: Update README with setup guide`)
* `refactor:` Code changes that neither fix a bug nor add a feature
* `test:` Adding or fixing tests
* `ci:` Changes to GitHub Actions or Docker files

**Example Commit:**
```bash
git commit -m "feat(api): Add /history endpoint
>
> Implements the /history GET endpoint to retrieve all
> verified claims from the sqlite database."
````

## 4\. Submitting a Pull Request

1.  Push your feature branch to your fork.
2.  Open a Pull Request (PR) from your branch to the main repo's `develop` branch.
3.  Ensure the GitHub Actions (CI) tests pass.
4.  Link the PR to the GitHub Issue it resolves (e.g., "Closes \#1").

<!-- end list -->

```

---

### Your Next Step

Your "documentation" is now planned. The next logical step from your `PLAN.md` is:

**Week 1, Task 3: `requirements.txt` & Python `venv` setup**

Shall we create the `requirements.txt` file now?
```
