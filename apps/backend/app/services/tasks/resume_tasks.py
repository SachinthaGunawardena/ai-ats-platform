from app.workers.celery_worker import celery
from app.database.session import SessionLocal
from app.models.resume import Resume

from app.services.parsing.resume_parser import extract_text_from_resume
from app.workers.celery_worker import celery
from app.database.session import SessionLocal
from app.models.resume import Resume
from app.services.parsing.resume_parser import extract_text_from_resume

import traceback


@celery.task
def process_resume(resume_id: int):

    db = SessionLocal()

    try:
        # STEP A — Fetch Resume
        resume = (
            db.query(Resume)
            .filter(Resume.id == resume_id)
            .first()
        )

        if not resume:
            print("Resume not found")
            return

        # Update status → processing
        resume.status = "processing"
        db.commit()

        # STEP B — Read File Path
        file_path = resume.file_path

        # STEP C — Extract Text
        extracted_text = extract_text_from_resume(
    resume.file_path,
    resume.filename
)

        # STEP D — Save Extracted Text
        resume.extracted_text = extracted_text

        # STEP E — Update Status
        resume.status = "processed"

        db.commit()

        print(f"Resume {resume.id} processed successfully")

    except Exception as e:
        print("ERROR:", str(e))

        if resume:
            resume.status = "failed"
            db.commit()

    finally:
        db.close()