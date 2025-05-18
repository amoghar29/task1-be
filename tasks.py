from celery_app import celery 
import db.redis as r



def fetch_task_from_redis():
    job = r.lpop("job_queue")
    if job:
        print(job)
