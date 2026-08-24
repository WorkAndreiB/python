import requests
import json

board_token = "canonical"

url = f"https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs"

response = requests.get(url, params={"content": "true"}, timeout=10)

# parameters={
#     "language": "cpp",
#     "location": "Romania",
# }

#automatically converts the parameters dictionary into a query string and appends it to the URL
# response = requests.get("https://httpbin.org/status/404", params=parameters, timeout=10)

# If the server returned an HTTP error, stop here and raise an exception.
response.raise_for_status()

# print(type(parameters))
# print(response.url)

data = response.json()
print(type(data))
print(data.keys())
print("Number of jobs:", len(data["jobs"]))

first_job = data["jobs"][0]
print("First job:", first_job["title"]) 
print("First job location:", first_job["location"]["name"])


print(type(data["jobs"]))

keywords = [
    "c++",
    "embedded",
    "robotics",
]

for job in data["jobs"]:
    if any(keyword.lower() in job["title"].lower() for keyword in keywords):
        print("Relevant job found:")
        print(job["title"], "at", job["location"]["name"], "-", job["absolute_url"])
        print()

print("First job details:")

print(type(data["jobs"][0]))
print(data["jobs"][0])