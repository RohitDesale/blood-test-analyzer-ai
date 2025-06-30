# crud.py
from sqlalchemy.orm import Session
from datetime import datetime

from models import AnalysisResult
from schema import AnalysisResultCreate

def save_analysis_result(
    db: Session,
    user_id: str,
    file_name: str,
    query: str,
    result: str,
    timestamp: datetime
):
    db_result = AnalysisResult(
        user_id=user_id,
        file_name=file_name,
        query=query,
        result=result,
        timestamp=timestamp
    )
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

def get_all_results(db: Session):
    return db.query(AnalysisResult).all()

def get_result_by_user_id(db: Session, user_id: str):
    return db.query(AnalysisResult).filter(AnalysisResult.user_id == user_id).all()

def get_result_by_id(db: Session, id: int):
    return db.query(AnalysisResult).filter(AnalysisResult.id == id).first()

def delete_result_by_id(db: Session, id: int):
    result = db.query(AnalysisResult).filter(AnalysisResult.id == id).first()
    if result:
        db.delete(result)
        db.commit()
        return True
    return False
