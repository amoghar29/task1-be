from celery_app import Celery

celery = Celery(
    "tasks",
)
celery.conf.beat_schedule = {}
celery.conf.timezone = "UTC"

from celery.schedules import crontab

celery.conf.beat_schedule = {
    "fetch-every-10-seconds": {
        "task": "tasks.fetch_from_redis_and_send",
        "schedule": 10.0,
    },
}
