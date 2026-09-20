import json
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parents[3]
ROLE_FILE = BASE_DIR / "data" / "role_requirements.json"


def load_role_requirements() -> dict[str, Any]:
    with open(ROLE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def calculate_skill_gap(
    current_skills: list[str],
    target_role: str
) -> dict[str, Any]:

    roles = load_role_requirements()

    if target_role not in roles:
        return {
            "error": f"Target role '{target_role}' is not supported.",
            "available_roles": list(roles.keys())
        }

    required_skills = roles[target_role]["required_skills"]

    current_normalized = {
        skill.lower(): skill
        for skill in current_skills
    }

    matched = []
    missing = []

    for skill in required_skills:

        if skill.lower() in current_normalized:
            matched.append(skill)
        else:
            missing.append(skill)

    total = len(required_skills)
    matched_count = len(matched)

    readiness = round(
        (matched_count / total) * 100,
        2
    ) if total else 0

    if readiness >= 80:
        overall_priority = "Low"
    elif readiness >= 50:
        overall_priority = "Medium"
    else:
        overall_priority = "High"

    return {
        "target_role": target_role,
        "required_skills": required_skills,
        "current_matching_skills": matched,
        "missing_skills": missing,
        "matched_count": matched_count,
        "missing_count": len(missing),
        "readiness_percentage": readiness,
        "overall_priority": overall_priority
    }