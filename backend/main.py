
from fastapi import FastAPI

app = FastAPI(
    title="Himalaya Climate Security",
    description="Early Warning System for the Himalayan Region",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "project": "Early Warning System and Climate Security for Himalayas",
        "status": "Development Started",
        "ai_used": False
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "system": "Himalaya Climate Security"
    }
