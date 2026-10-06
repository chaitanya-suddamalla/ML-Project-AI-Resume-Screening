# AI-Based Resume Screening and Job Matching System

**BTech Computer Science & Engineering (CSE) Final Year Capstone Project**

---

## 📌 1. Project Abstract & Objective
The **AI-Based Resume Screening and Job Matching System** is a full-stack, Natural Language Processing (NLP) powered web application designed to evaluate candidate resumes against target job descriptions. Using term frequency-inverse document frequency (**TF-IDF**) vectorization, **Cosine Similarity**, phrase matching algorithms, and canonical synonym maps, the system provides transparent skill breakdown metrics, identifies critical missing skill gaps, and generates a persistent personalized learning roadmap.

> **Ethics & Fairness Disclaimer**: This platform functions strictly as an educational and career-assistance diagnostic tool. It does **NOT** compute hiring probabilities, infer candidate suitability, or measure personal traits. Personal Identifiable Information (PII) such as emails and phone numbers are automatically sanitized upon document ingestion to safeguard candidate privacy.

---

## 🏗️ 2. Technology Stack

### Backend & Machine Learning
- **Framework**: Python 3.14 + FastAPI
- **Web Server**: Uvicorn
- **Database & ORM**: SQLite3 + SQLAlchemy 2.0
- **Document Parsing**: PyMuPDF (`pymupdf`/`fitz`) for PDF, `python-docx` for DOCX, UTF-8 plain text parser
- **NLP & Machine Learning**: `scikit-learn` (`TfidfVectorizer`, `cosine_similarity`), `pandas`, `numpy`, `joblib`
- **Optional Semantic Matcher**: `sentence-transformers` (`all-MiniLM-L6-v2`) with TF-IDF fallback
- **Testing**: `pytest`, `httpx`

### Frontend
- **Framework**: React.js 18 + Vite
- **Styling**: Tailwind CSS, Glassmorphic UI design tokens
- **Data Visualization**: Custom SVG gauge charts & Recharts
- **Icons**: Lucide React

---

## 🏛️ 3. System Architecture & Workflow

```mermaid
graph TD
    User[User / CSE Student] -->|Upload PDF/DOCX/TXT Resume| Parser[Document Parser & PII Sanitizer]
    User -->|Paste Job Specs| JobEngine[Job Spec Validator]
    Parser -->|Clean Text| NLP[NLP & Vectorization Pipeline]
    JobEngine -->|Clean Specs| NLP
    
    subgraph NLP Pipeline
        NLP --> Prep[Technical Token Preservation: C++, C#, .NET, React.js]
        Prep --> TFIDF[TF-IDF N-Gram Vectorizer (1, 2)]
        TFIDF --> Cosine[Cosine Similarity Calculation]
        NLP --> SkillExt[Phrase Boundary Skill Extractor & Synonym Mapper]
    end
    
    Cosine --> Score[Text Similarity Score & Percentage]
    SkillExt --> Categorizer[Skill Categorizer: Matched, Missing, Resume-Only]
    Categorizer --> Roadmap[Personalized Learning Checklist Generator]
    
    Score --> DB[(SQLite Database via SQLAlchemy)]
    Categorizer --> DB
    Roadmap --> DB
    
    DB --> ReactUI[React + Vite Frontend Dashboard]
```

---

## 📊 4. Database Schema (SQLite + SQLAlchemy)

The application persists all data across five linked tables:
1. `resumes`: Metadata, file type, character count, PII-sanitized raw text.
2. `job_descriptions`: Saved job descriptions for reuse.
3. `analysis_results`: Analysis run logs, similarity scores, keyword baseline scores, matched/missing skill JSON blobs.
4. `learning_checklist_items`: Actionable skill gap learning items linked to analyses with status tracking (`Not Started`, `In Progress`, `Completed`).

---

## 🔌 5. API Documentation

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/health` | System health status & DB connectivity |
| `POST` | `/api/v1/resume/upload` | Upload PDF/DOCX/TXT resume, sanitize PII & parse text |
| `POST` | `/api/v1/jobs` | Save job description for reuse |
| `GET` | `/api/v1/jobs` | Retrieve saved job descriptions |
| `POST` | `/api/v1/analyze` | Execute full NLP resume vs job description matching |
| `GET` | `/api/v1/analyses` | Fetch historical analysis records |
| `GET` | `/api/v1/analyses/{id}` | Fetch specific analysis detail and checklist |
| `DELETE` | `/api/v1/analyses/{id}` | Delete analysis record & checklist items |
| `GET` | `/api/v1/skills` | Retrieve transparent skill catalog dictionary |
| `POST` | `/api/v1/skills` | Register new custom skill and synonyms to dictionary |
| `PATCH` | `/api/v1/learning-checklist/{item_id}` | Update skill roadmap item progress status |
| `GET` | `/api/v1/evaluation` | Model evaluation benchmarks, precision/recall stats |

---

## ⚡ 6. Windows Installation & Setup Guide

### Step 1: Clone or Navigate to Project Folder
```powershell
cd C:\Users\geeth\.gemini\antigravity\scratch\ai-resume-job-matcher
```

### Step 2: Set Up Backend
```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m pytest tests -v
python -m uvicorn app.main:app --reload --port 8000
```
*Backend server will run at: `http://localhost:8000` (API Docs: `http://localhost:8000/docs`)*

### Step 3: Set Up Frontend (In a New PowerShell Terminal)
```powershell
cd C:\Users\geeth\.gemini\antigravity\scratch\ai-resume-job-matcher\frontend
npm install
npm run dev
```
*Frontend dev server will run at: `http://localhost:5173`*

---

## 🧪 7. Automated Testing Suite

Run full automated tests using `pytest`:
```powershell
cd backend
.\venv\Scripts\python.exe -m pytest tests -v
```
All 12 unit and integration tests cover:
- Document extraction for PDF, DOCX, TXT.
- Empty & unreadable file handling.
- PII email, phone, and URL sanitization.
- Technical token regex protection (`C++`, `C#`, `.NET`, `React.js`, `CI/CD`).
- TF-IDF vectorization & Cosine similarity math.
- Skill phrase matching and synonym canonical normalization.
- FastAPI REST endpoint status codes and error responses.

---

## 🎯 8. BTech CSE Viva Questions & Answers

### Q1: What is the primary objective of this project?
**Answer:** To build an automated career-assistance web application that uses NLP techniques (TF-IDF vectorization and phrase matching) to compare candidate resumes against job descriptions, highlight matching skills, identify skill gaps, and provide a persistent personalized learning roadmap.

### Q2: Why is TF-IDF chosen over basic keyword counting?
**Answer:** Basic keyword counting treats all terms equally. TF-IDF (Term Frequency-Inverse Document Frequency) weights terms by how frequently they appear in a document relative to their rarity across the corpus. This downweights generic common words while emphasizing domain-specific technical terms like "FastAPI" or "Docker".

### Q3: How is Cosine Similarity calculated mathematically?
**Answer:** Cosine similarity measures the cosine of the angle between two multi-dimensional term vectors $\vec{A}$ and $\vec{B}$:
$$\text{Cosine Similarity}(\vec{A}, \vec{B}) = \frac{\vec{A} \cdot \vec{B}}{\|\vec{A}\| \|\vec{B}\|} = \frac{\sum_{i=1}^{n} A_i B_i}{\sqrt{\sum_{i=1}^{n} A_i^2} \sqrt{\sum_{i=1}^{n} B_i^2}}$$
The result ranges from $0$ (completely orthogonal/unrelated) to $1$ (identical term direction).

### Q4: How does the system handle special technical tokens like C++ and C#?
**Answer:** Standard tokenizer regex strips non-alphanumeric characters, turning `C++` into `C` and `C#` into `C`. Our custom preprocessor (`app/ml/preprocessing.py`) preserves technical tokens prior to tokenization by mapping `C++` $\rightarrow$ `cplusplus`, `C#` $\rightarrow$ `csharp`, `.NET` $\rightarrow$ `dotnet`, and `React.js` $\rightarrow$ `reactjs`.

### Q5: How are skill synonyms handled?
**Answer:** The system maintains a transparent skill catalog in `data/skills.json`. Every skill entry maps canonical variations (e.g. `React.js`, `ReactJS`, `React JS`) to the standard skill name `React`. This ensures candidates are not penalized for minor spelling variations.

### Q6: How does the system guarantee privacy and ethical NLP compliance?
**Answer:** The document parser automatically strips PII (emails, phone numbers, external portfolio URLs) upon document ingestion. Additionally, the system explicitly labels similarity scores as "Text Similarity Scores" rather than hiring probabilities, preventing unethical automated bias.

---

## 📄 License
Academic Capstone Project &copy; 2026. All rights reserved.
