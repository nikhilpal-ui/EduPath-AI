from typing import Any


def evaluate_progress(
    skill: str,
    score: float,
    completed: bool = True
) -> dict[str, Any]:

    # Validate score
    score = max(0, min(100, score))

    if not completed:
        status = "not_completed"
        recommendation = f"Continue practicing {skill}."
        additional_practice = True
        roadmap_action = f"Keep {skill} in the current learning phase."

    elif score < 50:
        status = "struggling"
        recommendation = (
            f"You are struggling with {skill}. "
            f"Review the fundamentals and complete additional practice."
        )
        additional_practice = True
        roadmap_action = (
            f"Extend {skill} practice and delay the next advanced topic."
        )

    elif score < 75:
        status = "needs_improvement"
        recommendation = (
            f"Your {skill} foundation is developing. "
            f"Complete targeted practice before moving forward."
        )
        additional_practice = True
        roadmap_action = (
            f"Add targeted {skill} practice before the next topic."
        )

    else:
        status = "mastered"
        recommendation = (
            f"Good progress in {skill}. "
            f"You can continue to the next topic."
        )
        additional_practice = False
        roadmap_action = (
            f"Continue the roadmap and move beyond {skill}."
        )

    return {
        "skill": skill,
        "score": score,
        "completed": completed,
        "status": status,
        "recommendation": recommendation,
        "additional_practice": additional_practice,
        "roadmap_action": roadmap_action
    }


def generate_adaptive_plan(
    results: list[dict[str, Any]]
) -> dict[str, Any]:

    evaluated_results = []

    struggling_skills = []
    improving_skills = []
    mastered_skills = []

    for result in results:

        evaluation = evaluate_progress(
            skill=result["skill"],
            score=result["score"],
            completed=result.get("completed", True)
        )

        evaluated_results.append(evaluation)

        if evaluation["status"] == "struggling":
            struggling_skills.append(evaluation["skill"])

        elif evaluation["status"] == "needs_improvement":
            improving_skills.append(evaluation["skill"])

        elif evaluation["status"] == "mastered":
            mastered_skills.append(evaluation["skill"])

    if struggling_skills:
        overall_action = (
            "Reinforce struggling skills before progressing "
            "to advanced topics."
        )
    elif improving_skills:
        overall_action = (
            "Continue targeted practice for skills that need improvement."
        )
    else:
        overall_action = (
            "Learner is progressing well. Continue with the planned roadmap."
        )

    return {
        "results": evaluated_results,
        "struggling_skills": struggling_skills,
        "skills_needing_improvement": improving_skills,
        "mastered_skills": mastered_skills,
        "overall_action": overall_action
    }