from models import Job
from config import GREENHOUSE_COMPANIES, KEYWORDS, EXCLUDED_KEYWORDS
from filters.filters import is_relevant

from sources.greenhouse import fetch_jobs_from_greenhouse


def main():
    all_jobs = []
    for company in GREENHOUSE_COMPANIES:
        try:
            jobs = fetch_jobs_from_greenhouse(company["board_token"], company["name"])
            all_jobs.extend(jobs)
        except Exception as err:
            print(f"Error fetching jobs for {company['name']}: {err}")    
        
    relevant_jobs = [job for job in all_jobs if is_relevant(job, KEYWORDS, EXCLUDED_KEYWORDS)]

    print(f"Found {len(relevant_jobs)} relevant jobs:")
    for job in relevant_jobs:
        print(f"- {job.title}")
    

if __name__ == "__main__":
    main()