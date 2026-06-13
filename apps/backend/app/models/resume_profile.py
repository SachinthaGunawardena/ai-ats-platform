from sqlalchemy import Column, Integer, String, JSON
from app.database.session import Base


class ResumeProfile(Base):

    __tablename__ = "resume_profiles"

    id = Column(Integer, primary_key=True)

    email = Column(String)

    phone = Column(String)

    skills = Column(JSON)

    education = Column(JSON)

    experience_years = Column(Integer)