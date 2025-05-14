from celery_app import celery 
from db.redis import r


@celery.task()
def print_tasks(name):
    print(name)

@celery.task
def fetch_task_from_redis():
    job = r.lpop("job_queue")
    if job:
        print_tasks.delay(job)
