from sqlalchemy.orm import Session

from app.models.candidate import Candidate
from app.schemas.candidate import CandidateCreate


class CandidateRepository:

    @staticmethod
    def create(db: Session, candidate_data: CandidateCreate):
        candidate = Candidate(**candidate_data.model_dump())

        db.add(candidate)

        db.commit()

        db.refresh(candidate)

        return candidate

    @staticmethod
    def get_all(db: Session):
        return db.query(Candidate).all()