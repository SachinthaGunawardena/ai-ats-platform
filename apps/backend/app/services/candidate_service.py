from sqlalchemy.orm import Session

from app.repositories.candidate_repository import CandidateRepository
from app.schemas.candidate import CandidateCreate


class CandidateService:

    @staticmethod
    def create_candidate(db: Session, candidate_data: CandidateCreate):
        return CandidateRepository.create(db, candidate_data)

    @staticmethod
    def get_candidates(db: Session):
        return CandidateRepository.get_all(db)