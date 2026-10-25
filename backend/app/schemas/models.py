from pydantic import BaseModel, EmailStr
from typing import Optional, List


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str = "candidate"


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class ResumeExtracted(BaseModel):
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    summary: Optional[str] = None
    skills: List[str] = []
    education: List[str] = []
    experience: List[str] = []
    projects: List[str] = []
    certifications: List[str] = []
    confidence_score: float = 0.0


class InterviewConfig(BaseModel):
    role: str
    interview_type: str = "technical"
    difficulty: str = "medium"
    total_questions: int = 5
    job_description: Optional[str] = None


class SubmitAnswer(BaseModel):
    question_id: int
    answer_text: str


class MonitorEvent(BaseModel):
    event_type: str
    detail: Optional[str] = None
    confidence: float = 0.0
