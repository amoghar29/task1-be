from fastapi import APIRouter
from models.job import Job
from db.mongo import job_collection
from schema.schema import list_serial
import datetime

router = APIRouter()


# get req
@router.get("/jobs")
async def get_jobs():
    jobs_cursor = job_collection.find()
    jobs = []
    async for job in jobs_cursor:
        jobs.append(job)
    return list_serial(jobs)


@router.post("/jobs")
async def post_jobs(job: Job) -> dict:
    job_dict = dict(job)
    # Convert date objects to datetime objects
    if "start_date" in job_dict:
        job_dict["start_date"] = datetime.datetime.combine(
            job_dict["start_date"], datetime.time.min
        )
    if "end_date" in job_dict:
        job_dict["end_date"] = datetime.datetime.combine(
            job_dict["end_date"], datetime.time.min
        )

    res = await job_collection.insert_one(job_dict)
    return {"id": str(res.inserted_id)}
