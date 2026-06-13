from typing import Optional
from pydantic import BaseModel


class ResumeProfile(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

    skills: list[str] = []

    education: list[str] = []

    experience_years: Optional[int] = None