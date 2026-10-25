from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import InterviewSession, Question, Answer, Evaluation, MonitoringEvent
from app.schemas.models import InterviewConfig, SubmitAnswer, MonitorEvent
from app.services.interview_service import generate_questions_for_resume
from app.services.gemini_service import generate_answer_feedback

router = APIRouter()


@router.post("/generate")
def generate_interview(config: InterviewConfig, db: Session = Depends(get_db)):
    profile = db.query(Question).first()
    if not profile:
        questions = generate_questions_for_resume(None, config.role, config.interview_type, config.difficulty, config.total_questions, config.job_description)
        return {"questions": questions}
    return {"questions": ["Tell me about your experience with distributed systems.", "How do you handle performance bottlenecks?", "Describe a complex bug you solved."]}


@router.post("/start")
def start_session(user_id: int, role: str, interview_type: str, difficulty: str, db: Session = Depends(get_db)):
    session = InterviewSession(user_id=user_id, role=role, interview_type=interview_type, difficulty=difficulty, status="active", total_questions=5)
    db.add(session)
    db.commit()
    db.refresh(session)
    return {"session_id": session.id, "status": "active"}


@router.post("/submit-answer")
def submit_answer(payload: SubmitAnswer, db: Session = Depends(get_db)):
    question = db.query(Question).filter(Question.id == payload.question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    answer = Answer(question_id=payload.question_id, text=payload.answer_text)
    db.add(answer)
    db.commit()
    db.refresh(answer)

    feedback = generate_answer_feedback(payload.answer_text, question.question_text)
    return {"answer_id": answer.id, "feedback": feedback}


@router.post("/complete")
def complete_session(session_id: int, db: Session = Depends(get_db)):
    session = db.query(InterviewSession).filter(InterviewSession.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    session.status = "completed"
    db.commit()
    return {"message": "Interview completed", "session_id": session_id}


@router.post("/monitor")
def log_monitor_event(payload: MonitorEvent, db: Session = Depends(get_db)):
    event = MonitoringEvent(
        session_id=1,
        event_type=payload.event_type,
        detail=payload.detail,
        confidence=payload.confidence,
    )
    db.add(event)
    db.commit()
    return {"message": "Event logged"}
