from app.workers.celery_worker import celery
from app.database.session import SessionLocal
from app.models.resume import Resume

from app.services.parsing.resume_parser import extract_text_from_resume

import traceback


@celery.task
def process_resume(resume_id: int):

    db = SessionLocal()

    try:

        resume = db.query(Resume).filter(
            Resume.id == resume_id
        ).first()

        if not resume:
            return

        extracted_text = extract_text_from_resume(
            resume.file_path,
            resume.filename
        )

        resume.extracted_text = extracted_text
        resume.status = "processed"

        db.commit()

    except Exception as e:

        print("ERROR PROCESSING RESUME")
        print(str(e))

        traceback.print_exc()

        resume.status = "failed"

        db.commit()

    finally:
        db.close()