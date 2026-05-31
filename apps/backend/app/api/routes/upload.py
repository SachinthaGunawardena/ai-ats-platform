from fastapi import APIRouter, UploadFile, File
from app.services.storage.minio_service import client
import io

router = APIRouter()


@router.post("/resume")
async def upload_resume(file: UploadFile = File(...)):

    contents = await file.read()

    client.put_object(
        "resumes",
        file.filename,
        io.BytesIO(contents),
        length=len(contents),
        content_type=file.content_type
    )

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "Resume uploaded successfully"
    }