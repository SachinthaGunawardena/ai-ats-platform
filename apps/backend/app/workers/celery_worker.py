from celery import Celery

celery = Celery(
    "worker",
    broker="redis://redis:6379/0",
    include=["app.services.tasks.resume_tasks"]
)