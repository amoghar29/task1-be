from fastapi import FastAPI
from routes.job_routes import router
from db.mongo import client
import asyncio
from cron import job_checker


app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def start_bg_job_checker():
    asyncio.create_task(job_checker())


@app.on_event("startup")
async def startup_db_client():
    try:
        await client.admin.command("ping")
        print("✅ Connected to MongoDB!")
    except Exception as e:
        print(f"❌ Failed to connect to MongoDB: {e}")
