FairHire – Responsible AI for Resume Screening

FairHire is a full-stack resume screening system designed to promote privacy, fairness, and transparency in AI-powered hiring. It integrates PII redaction, machine learning–based evaluation, and real-time bias auditing into a unified, auditable workflow.

Project Highlights

- PII Redaction – Automatically detects and removes personally identifiable information (e.g., names, emails, phone numbers) before analysis.
- ML-Based Ranking – Scores resumes using a trained model based on experience, skills, and relevance.
- Bias Auditing – Evaluates whether scores are disproportionately low for specific demographic groups (e.g., gender or ethnicity).
- Explainability – Provides transparent justifications for each score to support accountability.
- Purpose Limitation – Logs access and enforces responsible data usage policies.

Tech Stack
| Layer          | Technologies 
| Backend        | Python, FastAPI, Pydantic, Uvicorn 
| Frontend       | React, Axios 
| ML**           | Scikit-learn (Logistic Regression), Fairlearn (Bias Audit), Pandas 
| Security & PII | Regex, Custom Redaction Logic 
| Deployment     | Docker 

Sample Workflow

1. HR uploads resumes via the frontend interface.
2. PII is detected and redacted server-side before analysis.
3. Cleaned resumes are scored by an ML model.
4. The system performs a bias audit on scores using group labels (e.g., A vs B).
5. Explanations and scores are returned to the user.
6. All access is logged to support purpose limitation.

Evaluation Metrics

- PII Redaction
  - Precision / Recall on test resumes
- Bias Detection
  - Demographic parity difference
  - Disparate impact ratio
- Model Performance
  - Accuracy / F1-score (optional on labeled data)
- Explainability
  - Per-score rationale
  - Audit logs for transparency

Why This Matters

FairHire demonstrates how to:
- Build ethical AI systems with fairness and accountability in mind
- Apply privacy-by-design principles in real-world workflows
- Integrate machine learning and governance into usable tools
- Work across disciplines: data science, ethics, policy, and UX

Getting Started

1. Backend (FastAPI)

```bash
cd fairhire-backend
uvicorn app.main:app --reload
```
2. Frontend (React)

```bash
cd fairhire-frontend
npm install
npm start
```
