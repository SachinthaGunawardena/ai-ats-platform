from fastapi import APIRouter, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4

import tempfile
import os
import io

from app.services.storage.minio_service import client
from app.database.session import SessionLocal
from app.models.resume import Resume
from app.services.tasks.resume_tasks import process_resume
from app.core.logger import logger

router = APIRouter()


@router.post("/resume")
async def upload_resume(file: UploadFile = File(...)):

    db: Session = SessionLocal()

    try:

        contents = await file.read()

        # Validate empty file
        if not contents:
            raise HTTPException(
                status_code=400,
                detail="Empty file uploaded"
            )

        # Validate extension
        allowed_extensions = [".pdf", ".docx"]

        suffix = os.path.splitext(file.filename)[1].lower()

        if suffix not in allowed_extensions:
            raise HTTPException(
                status_code=400,
                detail="Unsupported file format"
            )

        # Validate size
        max_size = 10 * 1024 * 1024

        if len(contents) > max_size:
            raise HTTPException(
                status_code=400,
                detail="File size exceeds 10MB"
            )

        # Generate UUID filename
        unique_filename = f"{uuid4()}{suffix}"

        # Production-style folder structure
        company_id = 1
        candidate_id = 1

        object_path = (
            f"resumes/{company_id}/"
            f"{candidate_id}/"
            f"{unique_filename}"
        )

        uploads_dir = "uploads"
        os.makedirs(uploads_dir, exist_ok=True)

        file_path = os.path.join(
        uploads_dir,
        unique_filename
        )

        with open(file_path, "wb") as f:
            f.write(contents)

        # Upload to MinIO
        client.put_object(
            "resumes",
            object_path,
            io.BytesIO(contents),
            length=len(contents),
            content_type=file.content_type
        )

        # Save metadata
        resume = Resume(
    filename=file.filename,
    object_name=object_path,
    file_path=file_path,
    status="uploaded"
)

        db.add(resume)
        db.commit()
        db.refresh(resume)

        print("AFTER DB SAVE")
        print(f"Resume ID = {resume.id}")

        print("BEFORE CELERY")

        process_resume.delay(resume.id)

        print("AFTER CELERY")

        logger.info(f"Resume uploaded: {object_path}")

        return {
            "message": "Resume uploaded successfully",
            "resume_id": resume.id,
            "filename": resume.filename,
            "status": resume.status
        }

    except Exception as e:

        logger.error(str(e))

        raise HTTPException(
            status_code=500,
            detail="Failed to upload resume"
        )

    finally:
        db.close()