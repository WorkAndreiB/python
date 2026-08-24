from models import Job

def calculate_score(job: Job, scoring_criteria: dict) -> int:
    score = 0

    criterias = {
        "title": job.title.lower(),
        "description": job.description.lower(),
        "location": job.location.lower(),
    }
    
    for citeria, options in scoring_criteria.items():
        text_to_check = criterias[citeria]
        
        for keyword, points in options.items():
            if keyword.lower() in text_to_check:
                score += points
        


    return score