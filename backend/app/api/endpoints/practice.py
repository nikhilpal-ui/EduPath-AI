from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.services.practice_agent import generate_practice


router = APIRouter(
    prefix="/practice",
    tags=["Practice"]
)


class PracticeRequest(BaseModel):
    skills: list[str]
    tasks_per_skill: int = Field(default=3, ge=1, le=10)


@router.post("/generate")
async def generate_practice_tasks(request: PracticeRequest):

    practice = generate_practice(
        skills=request.skills,
        tasks_per_skill=request.tasks_per_skill
    )

    return {
        "skills": request.skills,
        "practice": practice
    }