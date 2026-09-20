from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.services.learning_objective_agent import generate_learning_objectives
from app.services.resource_agent import recommend_resources
from app.services.learning_planner import create_weekly_roadmap


router = APIRouter(
    prefix="/roadmap",
    tags=["Roadmap"]
)


class RoadmapRequest(BaseModel):
    missing_skills: list[str]
    weeks: int = Field(default=4, ge=1, le=12)
    hours_per_week: int = Field(default=10, ge=1, le=40)


@router.post("/generate")
async def generate_roadmap(request: RoadmapRequest):

    # Step 1: Generate learning objectives
    objectives = generate_learning_objectives(
        request.missing_skills
    )

    # Step 2: Recommend resources
    resources = recommend_resources(
        request.missing_skills
    )

    # Step 3: Create personalized roadmap
    roadmap = create_weekly_roadmap(
        learning_objectives=objectives,
        resources=resources,
        weeks=request.weeks,
        hours_per_week=request.hours_per_week
    )

    return {
        "missing_skills": request.missing_skills,
        "learning_objectives": objectives,
        "resources": resources,
        "roadmap": roadmap
    }