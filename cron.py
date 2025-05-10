from datetime import datetime
from db.mongo import job_collection
import asyncio
from db.redis import r 


async def job_checker():
    while True:
        now = datetime.utcnow()
        print(f"cron job running at {now}")
        jobs = job_collection.find({
            "start_date": {"$lte": now},
            "end_date": {"$gte": now},
            "next_run": {"$lte": now}
        })

        async for job in jobs:
            print(f"pushing job :{job['_id']} to Redis")
            r.lpush("job_queue",str(job["_id"]))
        await asyncio.sleep(15)