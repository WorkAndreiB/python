from models import Job, ScoredJob
from config import GREENHOUSE_COMPANIES, SCORING_CRITERIA
from scoring import calculate_score

from sources.greenhouse import fetch_jobs_from_greenhouse


def main():
    all_jobs = []
    for company in GREENHOUSE_COMPANIES:
        try:
            jobs = fetch_jobs_from_greenhouse(company["board_token"], company["name"])
            all_jobs.extend(jobs)
        except Exception as err:
            print(f"Error fetching jobs for {company['name']}: {err}")    
        
    
    relevant_jobs = []
    for job in all_jobs:
        score = calculate_score(job, SCORING_CRITERIA)
        if score > 5:
            relevant_jobs.append(ScoredJob(job=job, score=score))
    
    # Sort the relevant jobs by score in descending order
    # sorting is done based on the key value. 
    # key is a lamda function that takes a ScoredJob object and returns its score attribute.        
    relevant_jobs.sort(key=lambda scored_job: scored_job.score, reverse=True)
    

    print(f"Found {len(relevant_jobs)} relevant jobs:")
    for scored_job in relevant_jobs:
        print(f"- (Score: {scored_job.score})  {scored_job.job.title} at {scored_job.job.company}")
    

if __name__ == "__main__":
    main()