from typing import Any


def create_weekly_roadmap(
    learning_objectives: list[dict[str, Any]],
    resources: list[dict[str, Any]],
    weeks: int = 4,
    hours_per_week: int = 10
) -> dict[str, Any]:

    if not learning_objectives:
        return {
            "weeks": [],
            "total_weeks": 0,
            "hours_per_week": hours_per_week
        }

    roadmap = []

    # Flatten learning topics
    topics = []

    for objective in learning_objectives:
        skill = objective["skill"]

        for topic in objective.get("topics", []):
            topics.append({
                "skill": skill,
                "topic": topic
            })

    # Divide topics across requested weeks
    total_topics = len(topics)
    topics_per_week = max(1, (total_topics + weeks - 1) // weeks)

    topic_index = 0

    for week_number in range(1, weeks + 1):

        week_topics = topics[
            topic_index: topic_index + topics_per_week
        ]

        if not week_topics:
            break

        week_plan = []

        for item in week_topics:

            skill = item["skill"]
            topic = item["topic"]

            matching_resources = []

            for resource_group in resources:

                if resource_group.get("skill") == skill:

                    matching_resources.extend(
                        resource_group.get("resources", [])
                    )

            week_plan.append({
                "skill": skill,
                "topic": topic,
                "estimated_hours": round(
                    hours_per_week / len(week_topics),
                    1
                ),
                "resources": matching_resources[:2]
            })

        roadmap.append({
            "week": week_number,
            "focus": list(
                dict.fromkeys(
                    item["skill"] for item in week_topics
                )
            ),
            "total_hours": hours_per_week,
            "learning_tasks": week_plan,
            "practice_task": generate_practice_task(week_topics),
        })

        topic_index += topics_per_week

    return {
        "total_weeks": len(roadmap),
        "hours_per_week": hours_per_week,
        "roadmap": roadmap
    }


def generate_practice_task(
    topics: list[dict[str, str]]
) -> str:

    if not topics:
        return "Complete a practical exercise related to your learning objectives."

    skill_names = list(
        dict.fromkeys(
            item["skill"] for item in topics
        )
    )

    topic_names = [
        item["topic"]
        for item in topics
    ]

    if len(skill_names) == 1:

        skill = skill_names[0]

        return (
            f"Complete a practical exercise covering "
            f"{', '.join(topic_names)} using {skill}."
        )

    return (
        f"Complete a practical exercise covering "
        f"{', '.join(topic_names)} across "
        f"{', '.join(skill_names)}."
    )