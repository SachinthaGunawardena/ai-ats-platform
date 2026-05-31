from fastapi import FastAPI
from app.database.session import Base, engine

from app.models.candidate import Candidate
from app.models.resume import Resume
from app.models.job import Job

from app.api.routes import upload
from app.api.candidate_routes import router as candidate_router

app = FastAPI(title="AI ATS Platform")

Base.metadata.create_all(bind=engine)

app.include_router(candidate_router)
app.include_router(upload.router, prefix="/upload")


@app.get("/")
def root():
    return {"message": "AI ATS Backend Running"}