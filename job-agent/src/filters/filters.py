from models import Job
from config import KEYWORDS, EXCLUDED_KEYWORDS


def is_relevant(job: Job, keywords, excluded_keywords) -> bool:
    contains_keyword = any(keyword.lower() in job.title.lower() 
                           or keyword.lower() in job.description.lower() 
                           for keyword in keywords)

    contains_excluded_keyword = any(excluded_keyword.lower() in job.title.lower() 
                                    or excluded_keyword.lower() in job.description.lower() 
                                    for excluded_keyword in excluded_keywords)

    return contains_keyword and not contains_excluded_keyword