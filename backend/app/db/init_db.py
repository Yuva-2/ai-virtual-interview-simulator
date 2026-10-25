from app.db.session import Base, engine
from app.models.user import User
from app.models.resume import ResumeProfile
from app.models.interview import InterviewSession, Question, Answer, Evaluation, MonitoringEvent
from app.models.recruiter import RecruiterReport


def init_db() -> None:
    Base.metadata.create_all(bind=engine)
