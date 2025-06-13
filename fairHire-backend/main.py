# FastAPI backend that
# Accepts a resume upload, redacts PII, scores the resume, simulates a bias audit, logs all access

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from utils.redact import redact_pii
from utils.score import score_resume
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")

    redacted, pii = redact_pii(text)
    score, explanation = score_resume(redacted)

    log_access(file.filename, "score_resume")

    return {
        "filename": file.filename,
        "redacted": redacted,
        "pii_found": pii,
        "score": score,
        "explanation": explanation
    }

@app.get("/bias_audit")
def bias_audit():
    group_a_scores = [75, 80, 70]
    group_b_scores = [45, 50, 40]

    avg_a = sum(group_a_scores) / len(group_a_scores)
    avg_b = sum(group_b_scores) / len(group_b_scores)

    bias_warning = ""
    if abs(avg_a - avg_b) > 20:
        bias_warning = "⚠️ Potential bias detected"

    return {
        "group_a_avg": avg_a,
        "group_b_avg": avg_b,
        "bias_warning": bias_warning
    }

def log_access(filename: str, purpose: str):
    with open("logs/access.log", "a") as f:
        f.write(f"{datetime.now()} | File: {filename} | Purpose: {purpose}\n")
