from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.services.adaptive_progress_agent import (
    evaluate_progress,
    generate_adaptive_plan
)


router = APIRouter(
    prefix="/adaptive",
    tags=["Adaptive Learning"]
)


class ProgressRequest(BaseModel):
    skill: str
    score: float = Field(ge=0, le=100)
    completed: bool = True


class AdaptivePlanRequest(BaseModel):
    results: list[ProgressRequest]


@router.post("/evaluate")
async def evaluate_learning_progress(request: ProgressRequest):

    return evaluate_progress(
        skill=request.skill,
        score=request.score,
        completed=request.completed
    )


@router.post("/plan")
async def generate_adaptive_learning_plan(
    request: AdaptivePlanRequest
):

    results = [
        {
            "skill": item.skill,
            "score": item.score,
            "completed": item.completed
        }
        for item in request.results
    ]

    return generate_adaptive_plan(results)