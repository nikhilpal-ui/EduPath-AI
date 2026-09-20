from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.services.progress_agent import (
    update_progress,
    generate_progress_report
)

router = APIRouter(
    prefix="/progress",
    tags=["Progress Tracking"]
)


class ProgressItem(BaseModel):
    skill: str
    score: float = Field(ge=0, le=100)
    completed: bool = False


class ProgressReportRequest(BaseModel):
    required_skills: list[str]
    progress: list[ProgressItem]


@router.post("/update")
async def update_learning_progress(request: ProgressItem):
    return update_progress(
        skill=request.skill,
        score=request.score,
        completed=request.completed
    )


@router.post("/report")
async def create_progress_report(
    request: ProgressReportRequest
):
    progress = [
        {
            "skill": item.skill,
            "score": item.score,
            "completed": item.completed
        }
        for item in request.progress
    ]

    return generate_progress_report(
        required_skills=request.required_skills,
        progress=progress
    )