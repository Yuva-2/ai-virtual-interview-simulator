from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.session import Base


class ResumeProfile(Base):
    __tablename__ = "resume_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    full_name = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    phone = Column(String(100), nullable=True)
    skills = Column(Text, nullable=True)
    education = Column(Text, nullable=True)
    experience = Column(Text, nullable=True)
    projects = Column(Text, nullable=True)
    certifications = Column(Text, nullable=True)
    summary = Column(Text, nullable=True)
    file_name = Column(String(255), nullable=True)
    confidence_score = Column(Float, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    user = relationship("User", back_populates="profile")


class InterviewSession(Base):
    __tablename__ = "interview_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    role = Column(String(255), nullable=False)
    interview_type = Column(String(100), nullable=False)
    difficulty = Column(String(100), default="medium")
    status = Column(String(100), default="created")
    total_questions = Column(Integer, default=0)
    current_index = Column(Integer, default=0)
    started_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)

    user = relationship("User", back_populates="sessions")
    questions = relationship("Question", back_populates="session")
    evaluations = relationship("Evaluation", back_populates="session")
    monitoring_events = relationship("MonitoringEvent", back_populates="session")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("interview_sessions.id"), nullable=False)
    question_text = Column(Text, nullable=False)
    question_type = Column(String(100), default="technical")
    order_index = Column(Integer, default=0)

    session = relationship("InterviewSession", back_populates="questions")
    answers = relationship("Answer", back_populates="question")


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    text = Column(Text, nullable=False)
    score = Column(Float, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    question = relationship("Question", back_populates="answers")


class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("interview_sessions.id"), nullable=False)
    overall_score = Column(Float, default=0.0)
    summary = Column(Text, nullable=False)
    strengths = Column(Text, nullable=True)
    weaknesses = Column(Text, nullable=True)
    suggestions = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    session = relationship("InterviewSession", back_populates="evaluations")


class MonitoringEvent(Base):
    __tablename__ = "monitoring_events"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("interview_sessions.id"), nullable=False)
    event_type = Column(String(120), nullable=False)
    detail = Column(Text, nullable=True)
    confidence = Column(Float, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    session = relationship("InterviewSession", back_populates="monitoring_events")


class RecruiterReport(Base):
    __tablename__ = "recruiter_reports"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    recruiter_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    summary = Column(Text, nullable=False)
    score = Column(Float, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
