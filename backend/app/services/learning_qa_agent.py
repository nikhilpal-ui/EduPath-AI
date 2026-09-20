from typing import Any


def answer_learning_question(
    question: str,
    target_role: str,
    skill_gap: dict[str, Any],
    progress_report: dict[str, Any] | None = None
) -> dict[str, Any]:

    question_lower = question.lower()

    missing_skills = skill_gap.get("missing_skills", [])
    matched_skills = skill_gap.get("current_matching_skills", [])
    readiness = skill_gap.get("readiness_percentage", 0)

    if "what should i learn next" in question_lower or "learn next" in question_lower:
        if progress_report:
            in_progress = progress_report.get(
                "skills_in_progress", []
            )

            if in_progress:
                next_skill = in_progress[0]["skill"]

                answer = (
                    f"You should continue with {next_skill} first. "
                    f"After improving {next_skill}, move to the remaining "
                    f"skills required for {target_role}."
                )
            else:
                next_skill = (
                    missing_skills[0]
                    if missing_skills
                    else None
                )

                if next_skill:
                    answer = (
                        f"Your next priority should be {next_skill}. "
                        f"It is currently missing from your profile "
                        f"for the {target_role} role."
                    )
                else:
                    answer = (
                        f"You have covered the required skills for "
                        f"{target_role}. Your next step should be "
                        f"advanced projects and practical experience."
                    )
        else:
            next_skill = (
                missing_skills[0]
                if missing_skills
                else None
            )

            if next_skill:
                answer = (
                    f"Your next priority should be {next_skill}. "
                    f"It is one of the missing skills for your "
                    f"{target_role} goal."
                )
            else:
                answer = (
                    "Your required skills are covered. "
                    "Focus on advanced projects and practical experience."
                )

    elif "why" in question_lower and (
        "not ready" in question_lower
        or "ready" in question_lower
    ):
        if missing_skills:
            answer = (
                f"Your current readiness for {target_role} is "
                f"{readiness}%. You are missing "
                f"{', '.join(missing_skills)}. "
                f"Developing these skills will improve your "
                f"coverage of the target role requirements."
            )
        else:
            answer = (
                f"Your profile currently covers the required "
                f"skills for {target_role}."
            )

    elif "skill gap" in question_lower or "missing" in question_lower:
        if missing_skills:
            answer = (
                f"Your main skill gaps for {target_role} are: "
                f"{', '.join(missing_skills)}."
            )
        else:
            answer = (
                f"No major skill gaps were detected for "
                f"{target_role}."
            )

    elif "progress" in question_lower:
        if progress_report:
            answer = (
                f"Your current progress is "
                f"{progress_report.get('overall_progress_percentage', 0)}%. "
                f"You have "
                f"{len(progress_report.get('acquired_skills', []))} "
                f"acquired skills, "
                f"{len(progress_report.get('skills_in_progress', []))} "
                f"in-progress skills, and "
                f"{len(progress_report.get('remaining_skills', []))} "
                f"remaining skills."
            )
        else:
            answer = (
                "Generate your progress report first so I can "
                "evaluate your learning progress."
            )

    else:
        answer = (
            f"For your goal of becoming a {target_role}, "
            f"you currently have {len(matched_skills)} matching skills "
            f"and {len(missing_skills)} identified skill gaps. "
            f"Your current readiness is {readiness}%. "
            f"Focus on the missing skills in your personalized roadmap."
        )

    return {
        "question": question,
        "target_role": target_role,
        "answer": answer,
        "readiness_percentage": readiness,
        "missing_skills": missing_skills,
        "current_matching_skills": matched_skills
    }