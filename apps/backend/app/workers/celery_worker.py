from celery import Celery

celery = Celery(
    "worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

celery.conf.imports = (
    "app.services.tasks.resume_tasks",
)