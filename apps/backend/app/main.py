from fastapi import FastAPI

from app.api.candidate_routes import router as candidate_router

app = FastAPI(title="AI ATS Platform")


app.include_router(candidate_router)


@app.get("/")
def root():
    return {"message": "AI ATS Backend Running"}