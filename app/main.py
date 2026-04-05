from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()

jobs = {}

class TrainRequest(BaseModel):
    model: str
    dataset: str
    method: str

@app.get("/")
def root():
    return {"message": "Fine-tuning service is running"}

@app.post("/train")
def start_training(req: TrainRequest):
    job_id = str(uuid.uuid4())

    jobs[job_id] = {
        "status": "running",
        "model": req.model,
        "dataset": req.dataset,
        "method": req.method
    }

    return {
        "job_id": job_id,
        "status": "running",
        "message": "Training job created"
    }

@app.get("/status/{job_id}")
def get_status(job_id: str):
    if job_id not in jobs:
        return {"error": "job not found"}
    return jobs[job_id]

@app.get("/jobs")
def list_jobs():
    return jobs
