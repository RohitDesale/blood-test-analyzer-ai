# models.py
from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from db import Base

class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(100), index=True)
    file_name = Column(String(255))
    query = Column(Text)
    result = Column(Text)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())