from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class CandidateCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: Optional[str] = None


class CandidateResponse(BaseModel):
    id: int
    full_name: str
    email: str
    phone: Optional[str] = None
    resume_url: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True