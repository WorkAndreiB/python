KEYWORDS = [
    "c++",
    "cpp",
    "robotics",
    "embedded",
    "medical device",
    "adas",
]

EXCLUDED_KEYWORDS = [
    "frontend",
    "javascript",
    ".net",
    "sales",
    
]

GREENHOUSE_COMPANIES = [
    {
        "name": "Canonical",
        "board_token": "canonical",
    },
]

SCORING_CRITERIA = {
    "title": {
        "c++": 5,
        "cpp": 5,
        "robotics": 4,
        "embedded": 4,
        "medical device": 3,
        "adas": 3,
    },
    "description": {
        "c++": 3,
        "cpp": 3,
        "robotics": 2,
        "embedded": 2,
        "medical device": 2,
        "adas": 1,
    },
    "location":{
        "remote": 5,
        "romania": 4,
        "brasov": 3,    
        "bucharest": 2,
    }
}