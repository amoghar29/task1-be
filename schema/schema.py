def individual_serial(job) -> dict:
    return {
        "id": str(job["_id"]),
        "name": job["name"],
        "cron": job["cron"],
        "next_run":job["next_run"],
        "start_date": job["start_date"],
        "end_date": job["end_date"],
    }
def list_serial (jobs)-> list:
    return[individual_serial(job) for job in jobs]