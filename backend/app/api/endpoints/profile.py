from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

from app.db.models import User
from app.db.session import AsyncSessionLocal


router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)


class ProfileCreate(BaseModel):
    name: str
    email: EmailStr | None = None
    target_role: str | None = None
    experience_level: str | None = None
    career_goal: str | None = None


@router.post("/")
async def create_profile(profile: ProfileCreate):

    async with AsyncSessionLocal() as session:

        user = User(
            name=profile.name,
            email=profile.email,
            target_role=profile.target_role,
            experience_level=profile.experience_level,
            career_goal=profile.career_goal,
        )

        session.add(user)
        await session.commit()
        await session.refresh(user)

        return {
            "message": "Profile created successfully",
            "user_id": user.id,
            "profile": {
                "name": user.name,
                "email": user.email,
                "target_role": user.target_role,
                "experience_level": user.experience_level,
                "career_goal": user.career_goal,
            }
        }