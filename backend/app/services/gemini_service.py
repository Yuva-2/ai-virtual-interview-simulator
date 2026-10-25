from fastapi import APIRouter

router = APIRouter()


@router.get("/summary")
def summary():
    return {
        "total_interviews": 24,
        "completed_interviews": 19,
        "average_score": 84.3,
        "pass_rate": 78,
    }
