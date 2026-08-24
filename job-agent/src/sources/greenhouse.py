import requests
from models import Job

def fetch_jobs_from_greenhouse(board_token: str, company: str) -> list[Job]:
    url = f"https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs"

    response = requests.get(url, params={"content": "true"}, timeout=10)

    response.raise_for_status()

    data = response.json()

    jobs = []
    for job_data in data["jobs"]:
        job = Job(
            title=job_data["title"],
            company=company,
            location=job_data["location"]["name"],
            url=job_data["absolute_url"],
            description=job_data.get("content", ""),
        )
        jobs.append(job)

    return jobs
