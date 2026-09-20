from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel

from app.services.learning_qa_agent import answer_learning_question


router = APIRouter(
    prefix="/learning-qa",
    tags=["Learning Journey Q&A"]
)


class LearningQARequest(BaseModel):
    question: str
    target_role: str
    skill_gap: dict[str, Any]
    progress_report: dict[str, Any] | None = None


@router.post("/ask")
async def ask_learning_question(
    request: LearningQARequest
):
    return answer_learning_question(
        question=request.question,
        target_role=request.target_role,
        skill_gap=request.skill_gap,
        progress_report=request.progress_report
    )