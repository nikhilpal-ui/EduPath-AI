from fastapi import APIRouter
from pydantic import BaseModel

from app.services.skill_gap_agent import calculate_skill_gap


router = APIRouter(
    prefix="/skill-gap",
    tags=["Skill Gap"]
)


class SkillGapRequest(BaseModel):
    current_skills: list[str]
    target_role: str


@router.post("/analyze")
async def analyze_skill_gap(request: SkillGapRequest):

    result = calculate_skill_gap(
        current_skills=request.current_skills,
        target_role=request.target_role
    )

    return result