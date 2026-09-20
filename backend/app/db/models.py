from datetime import datetime

from sqlalchemy import String, Integer, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(String(100))

    email: Mapped[str | None] = mapped_column(
        String(150),
        unique=True,
        nullable=True
    )

    target_role: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True
    )

    experience_level: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    career_goal: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    skills = relationship(
        "Skill",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    skill_gaps = relationship(
        "SkillGap",
        back_populates="user",
        cascade="all, delete-orphan"
    )


class Skill(Base):
    __tablename__ = "skills"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    level: Mapped[float] = mapped_column(
        Float,
        default=0.0
    )

    source: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    user = relationship(
        "User",
        back_populates="skills"
    )


class SkillGap(Base):
    __tablename__ = "skill_gaps"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    skill_name: Mapped[str] = mapped_column(
        String(100)
    )

    current_level: Mapped[float] = mapped_column(
        Float,
        default=0.0
    )

    required_level: Mapped[float] = mapped_column(
        Float,
        default=0.0
    )

    gap_score: Mapped[float] = mapped_column(
        Float,
        default=0.0
    )

    priority: Mapped[str] = mapped_column(
        String(30),
        default="Medium"
    )

    user = relationship(
        "User",
        back_populates="skill_gaps"
    )