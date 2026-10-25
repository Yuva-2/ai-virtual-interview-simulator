from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import User

router = APIRouter()


@router.get("/candidates")
def list_candidates(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return {
        "candidates": [
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "role": user.role,
            }
            for user in users
        ]
    }


@router.get("/candidate-report/{user_id}")
def candidate_report(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"report": None}
    return {"report": {"user_id": user.id, "name": user.name, "summary": "Strong technical fundamentals and clear communication.", "score": 88.5}}
