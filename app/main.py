from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="AI Analytics Assistant",
    description="LLM + SQL + Workflow Orchestration API",
    version="1.0"
)

app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "running"}