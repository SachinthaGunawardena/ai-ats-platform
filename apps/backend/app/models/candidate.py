from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database.session import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False, index=True)

    phone = Column(String, nullable=True)

    resume_url = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)