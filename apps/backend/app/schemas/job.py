from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class JobCreate(BaseModel):
    title: str
    description: str
    requirements: Optional[str] = None


class JobResponse(BaseModel):
    id: int
    title: str
    description: str
    requirements: str | None
    created_at: datetime

    class Config:
        from_attributes = True