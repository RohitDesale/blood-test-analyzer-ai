
# worker.py
from celery import Celery
import os

# Celery app instance
def make_celery():
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    celery = Celery(
        "tasks",
        broker=redis_url,
        backend=redis_url
    )
    celery.conf.update(
        task_serializer='json',
        accept_content=['json'],
        result_serializer='json',
        timezone='UTC',
        enable_utc=True,
    )
    return celery

celery_app = make_celery()

from db import get_db
from crud import save_analysis_result
from main import run_crew

@celery_app.task(name="process_blood_report")
def process_blood_report_task(file_path: str, query: str, file_name: str):
    from datetime import datetime
    import uuid

    result = run_crew(query=query, file_path=file_path)

    # Simulate getting user_id or generate one
    user_id = str(uuid.uuid4())

    db = next(get_db())
    save_analysis_result(
        db=db,
        user_id=user_id,
        file_name=file_name,
        query=query,
        result=str(result),
        timestamp=datetime.utcnow()
    )

    return {"status": "success", "result": str(result)}
