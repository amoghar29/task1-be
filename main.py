from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.job_routes import router
from db.mongo import client as mongo_client
import asyncio
from cron import job_checker
from fastapi.testclient import TestClient


app = FastAPI()
test_client = TestClient(app)

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Temporarily allow all origins for debugging
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def start_bg_job_checker():
    asyncio.create_task(job_checker())


@app.on_event("startup")
async def startup_db_client():
    try:
        await mongo_client.admin.command("ping")
        print("✅ Connected to MongoDB!")
    except Exception as e:
        print(f"❌ Failed to connect to MongoDB: {e}")
