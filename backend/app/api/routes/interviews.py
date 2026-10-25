from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import ResumeProfile, InterviewSession, Question, Answer, Evaluation
from app.models.resume import ResumeProfile as ResumeProfileModel
from app.schemas.models import InterviewConfig, SubmitAnswer, MonitorEvent
from app.services.interview_service import generate_questions_for_resume
from app.services.gemini_service import generate_answer_feedback

router = APIRouter()


@router.get("/me")
def get_resume(user_id: int, db: Session = Depends(get_db)):
    profile = db.query(ResumeProfile).filter(ResumeProfile.user_id == user_id).first()
    if not profile:
        return {"profile": None}
    return {
        "profile": {
            "id": profile.id,
            "full_name": profile.full_name,
            "email": profile.email,
            "phone": profile.phone,
            "summary": profile.summary,
            "skills": profile.skills,
            "education": profile.education,
            "experience": profile.experience,
            "projects": profile.projects,
            "certifications": profile.certifications,
            "confidence_score": profile.confidence_score,
        }
    }


@router.post("/generate-questions")
def generate_questions(config: InterviewConfig, db: Session = Depends(get_db)):
    user = db.query(ResumeProfile).filter(ResumeProfile.id == 1).first()
    if not user:
        raise HTTPException(status_code=404, detail="No resume profile found")

    questions = generate_questions_for_resume(
        profile=user,
        role=config.role,
        interview_type=config.interview_type,
        difficulty=config.difficulty,
        total_questions=config.total_questions,
        job_description=config.job_description,
    )
    return {"questions": questions}
