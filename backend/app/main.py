from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth, resumes, interviews, recruiters, analytics
from app.db.init_db import init_db

app = FastAPI(title="AI Interview Simulator API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    init_db()

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(resumes.router, prefix="/api/resumes", tags=["resumes"])
app.include_router(interviews.router, prefix="/api/interviews", tags=["interviews"])
app.include_router(recruiters.router, prefix="/api/recruiters", tags=["recruiters"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["analytics"])

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "ai-interview-simulator"}
