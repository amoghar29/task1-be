from celery_app import celery 
import db.redis as r


@celery.task
def print_tasks(name):
    print(name)

def fetch_task_from_redis():
    job = r.lpop("job_queue")
    if job:
        print_tasks.delay(job)
