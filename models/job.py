from pydantic import BaseModel, Field
from datetime import date, datetime


class Job(BaseModel):
    name: str = Field(..., example="Daily Backup")
    cron: str = Field(..., example="0 0 * * *")
    next_run: datetime = Field(..., example="2025-05-08T00:00:00")
    start_date: date = Field(..., example="2025-05-01")
    end_date: date = Field(..., example="2025-05-01")
