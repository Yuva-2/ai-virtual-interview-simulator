from typing import List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

from app.core.security import create_access_token, decode_token
from app.db.session import get_db
from app.models.user import User, ResumeProfile
from app.schemas.models import UserCreate, UserLogin, TokenResponse, ResumeExtracted
from app.services.resume_service import parse_resume_text, extract_resume_profile
from app.services.gemini_service import generate_resume_summary

router = APIRouter()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


@router.post("/register", response_model=TokenResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        name=user.name,
        email=str(user.email),
        password_hash="hashed_placeholder",
        role=user.role,
    )
    from app.core.security import hash_password

    new_user.password_hash = hash_password(user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = create_access_token(str(new_user.id))
    return {"access_token": token, "token_type": "bearer"}


@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    existing = get_user_by_email(db, user.email)
    if not existing or not verify_password(user.password, existing.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(str(existing.id))
    return {"access_token": token, "token_type": "bearer"}


@router.post("/me")
def me(token: str):
    try:
        payload = decode_token(token)
        return {"user_id": payload.get("sub"), "token_valid": True}
    except Exception:
        raise HTTPException(status_code=401, detail="Unauthorized")


@router.post("/upload")
def upload_resume(file: UploadFile = File(...), db: Session = Depends(get_db), token: str = ""):
    try:
        from app.core.security import verify_password
        if not token:
            raise HTTPException(status_code=401, detail="Missing token")

        payload = decode_token(token)
        user_id = int(payload["sub"])

        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Only PDF resumes are supported")

        raw_bytes = file.file.read()
        text = parse_resume_text(raw_bytes)
        extracted = extract_resume_profile(text)
        profile = db.query(ResumeProfile).filter(ResumeProfile.user_id == user_id).first()

        if profile is None:
            profile = ResumeProfile(user_id=user_id, file_name=file.filename)
            db.add(profile)

        profile.full_name = extracted.full_name or profile.full_name
        profile.email = extracted.email or profile.email
        profile.phone = extracted.phone or profile.phone
        profile.summary = extracted.summary or profile.summary
        profile.skills = ", ".join(extracted.skills)
        profile.education = "; ".join(extracted.education)
        profile.experience = "; ".join(extracted.experience)
        profile.projects = "; ".join(extracted.projects)
        profile.certifications = "; ".join(extracted.certifications)
        profile.confidence_score = extracted.confidence_score
        db.commit()

        return {"message": "Resume uploaded successfully", "profile": extracted.model_dump()}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
