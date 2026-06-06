from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Job Matcher API")

class Developer(BaseModel):
    name: str
    skills: list[str]

class Job(BaseModel):
    title: str
    required_skills: list[str]

class MatchRequest(BaseModel):
    developer: Developer
    jobs: list[Job]

def calculate_match(dev_skills, required_skills):
    match = sum(1 for s in required_skills if s in dev_skills)
    return round((match / len(required_skills)) * 100, 1)

@app.get("/")
def read_root():
    return {"status": "Job Matcher API is running!"}

@app.post("/match")
def match_jobs(request: MatchRequest):
    results = []
    for job in request.jobs:
        score = calculate_match(request.developer.skills, job.required_skills)
        results.append({"title": job.title, "score": score})
    
    sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)
    
    return {
        "developer": request.developer.name,
        "matches": sorted_results
    }