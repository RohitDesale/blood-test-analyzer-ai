# schema.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AnalysisResultBase(BaseModel):
    user_id: str
    file_name: str
    query: str
    result: str
    timestamp: Optional[datetime]

class AnalysisResultCreate(AnalysisResultBase):
    pass

class AnalysisResultOut(AnalysisResultBase):
    id: int

    class Config:
        orm_mode = True