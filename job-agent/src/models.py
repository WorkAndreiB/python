from dataclasses import dataclass

@dataclass
class Job:
    title: str
    company: str
    location: str
    url: str
    description: str=""
    
@dataclass
class ScoredJob:
    job: Job
    score: int