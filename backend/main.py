from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
import os
import uuid
from datetime import datetime
import shutil

from celery_app import celery_app
from database import SessionLocal
from models import AnalysisResult

app = FastAPI(title="Blood Test Report Analyser with Celery & DB")

@app.get("/")
async def root():
    return {"message": "Blood Test Report Analyser API is running"}

@app.post("/analyze")
async def analyze_blood_report(
    file: UploadFile = File(...),
    query: str = Form(default="Summarise my Blood Test Report")
):
    """Uploads PDF and sends to Celery worker"""
    
    try:
        # Validate input
        if not file.filename.endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Only PDF files are allowed")

        # Ensure data directory exists
        os.makedirs("data", exist_ok=True)

        # Save file locally
        file_id = str(uuid.uuid4())
        filename = f"blood_test_report_{file_id}.pdf"
        file_path = os.path.join("data", filename)
        
        with open(file_path, "wb") as f:
            f.write(await file.read())

        # Send to background task
        task = celery_app.send_task(
            "worker.process_blood_report",
            args=[query, file_path, filename]
        )

        return {
            "status": "submitted",
            "task_id": task.id,
            "message": "File received. Analysis is processing in background."
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/results/{task_id}")
def get_analysis_result(task_id: str):
    """Fetch results from DB using Celery task_id"""
    try:
        db = SessionLocal()
        record = db.query(AnalysisResult).filter(AnalysisResult.task_id == task_id).first()
        if not record:
            return JSONResponse(status_code=202, content={"message": "Task is still processing or not found."})
        
        return {
            "status": "completed",
            "task_id": task_id,
            "query": record.query,
            "filename": record.filename,
            "result": record.result,
            "timestamp": record.timestamp.isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
