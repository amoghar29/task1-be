from celery import Celery

celery = Celery(
        "tasks",broker="redis://localhost:6379/0"
)
celery.conf.beat_schedule = {}
celery.conf.timezone = "UTC"

celery.autodiscover_tasks(["tasks"])

from celery.schedules import crontab

celery.conf.beat_schedule = {
    "fetch-every-10-seconds": {
        "task": "tasks.fetch_task_from_redis",
        "schedule": 10.0,
    },
}
