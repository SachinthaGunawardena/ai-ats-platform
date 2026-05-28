from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.deps import get_db
from app.schemas.candidate import (
    CandidateCreate,
    CandidateResponse
)
from app.services.candidate_service import CandidateService


router = APIRouter(prefix="/candidates", tags=["Candidates"])


@router.post("/", response_model=CandidateResponse)
def create_candidate(
    candidate_data: CandidateCreate,
    db: Session = Depends(get_db)
):
    return CandidateService.create_candidate(db, candidate_data)


@router.get("/", response_model=list[CandidateResponse])
def get_candidates(
    db: Session = Depends(get_db)
):
    return CandidateService.get_candidates(db)
