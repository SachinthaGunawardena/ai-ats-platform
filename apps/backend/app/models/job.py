from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.database.session import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    description = Column(Text, nullable=False)

    requirements = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)