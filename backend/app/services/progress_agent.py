from typing import Any


def update_progress(
    skill: str,
    score: float,
    completed: bool = False
) -> dict[str, Any]:

    score = max(0, min(100, score))

    if completed and score >= 75:
        status = "acquired"
    elif score > 0:
        status = "in_progress"
    else:
        status = "remaining"

    return {
        "skill": skill,
        "score": score,
        "completed": completed,
        "status": status
    }


def generate_progress_report(
    required_skills: list[str],
    progress: list[dict[str, Any]]
) -> dict[str, Any]:

    progress_map = {
        item["skill"].lower(): item
        for item in progress
    }

    acquired = []
    in_progress = []
    remaining = []

    for skill in required_skills:
        item = progress_map.get(skill.lower())

        if not item:
            remaining.append(skill)
            continue

        result = update_progress(
            skill=skill,
            score=item.get("score", 0),
            completed=item.get("completed", False)
        )

        if result["status"] == "acquired":
            acquired.append(result)
        elif result["status"] == "in_progress":
            in_progress.append(result)
        else:
            remaining.append(skill)

    total = len(required_skills)

    progress_percentage = round(
        (len(acquired) / total) * 100,
        2
    ) if total else 0

    if remaining:
        next_steps = [
            f"Continue learning {skill}."
            for skill in remaining[:3]
        ]
    elif in_progress:
        next_steps = [
            f"Improve {item['skill']} before moving to advanced topics."
            for item in in_progress[:3]
        ]
    else:
        next_steps = [
            "All required skills have been acquired.",
            "Continue with advanced projects and real-world practice."
        ]

    return {
        "overall_progress_percentage": progress_percentage,
        "acquired_skills": acquired,
        "skills_in_progress": in_progress,
        "remaining_skills": remaining,
        "next_steps": next_steps,
        "summary": {
            "total_required_skills": total,
            "acquired_count": len(acquired),
            "in_progress_count": len(in_progress),
            "remaining_count": len(remaining)
        }
    }