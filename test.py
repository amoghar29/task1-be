from datetime import date, datetime
from .main import test_client
from models.job import Job


def test_get_jobs():
    response = test_client.get("/jobs")

    assert response.status_code == 200
    jobs = response.json()
    assert isinstance(jobs, list)
    if jobs:
        assert "id" in jobs[0]
        assert "name" in jobs[0]
        assert "cron" in jobs[0]
        assert "next_run" in jobs[0]
        assert "start_date" in jobs[0]
        assert "end_date" in jobs[0]


def test_post_job():
    response = test_client.post(
        "/jobs",
        json={
            "name": "Daily Backup",
            "cron": "0 0 * * *",
            "next_run": "2025-05-08T00:00:00",
            "start_date": "2025-05-01",
            "end_date": "2025-05-01",
        },
    )

    assert response.status_code == 200
    assert response.json() == {"id": "681cd843bcd5383af1c765e7"}
