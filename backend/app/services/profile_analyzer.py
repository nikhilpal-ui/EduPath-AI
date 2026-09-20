import re
from typing import Any


# Skills that EduPath can detect from resume text.
KNOWN_SKILLS = [
    "Python",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Seaborn",
    "SQL",
    "MySQL",
    "Power BI",
    "DAX",
    "Power Query",
    "Excel",
    "Machine Learning",
    "Scikit-learn",
    "Data Cleaning",
    "EDA",
    "Exploratory Data Analysis",
    "Feature Engineering",
    "Data Visualization",
    "Git",
    "GitHub",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Cloud Computing",
]


def extract_skills(text: str) -> list[str]:
    """
    Detect known skills from resume text.
    """
    detected = []

    normalized_text = text.lower()

    for skill in KNOWN_SKILLS:
        if skill.lower() in normalized_text:
            detected.append(skill)

    return detected


def extract_projects(text: str) -> list[str]:
    """
    Extract project names from a resume's PROJECTS section.
    """
    projects = []

    match = re.search(
        r"PROJECTS(.*?)(?:CERTIFICATION|CERTIFICATIONS|EDUCATION|$)",
        text,
        re.IGNORECASE | re.DOTALL,
    )

    if not match:
        return projects

    section = match.group(1)

    for line in section.splitlines():
        line = line.strip()

        if not line:
            continue

        # Ignore bullet descriptions
        if line.startswith(("•", "-", "*")):
            continue

        # Project titles usually contain a technology separator "|"
        if "|" in line:
            project_name = line.split("|")[0].strip()

            if project_name and project_name not in projects:
                projects.append(project_name)

    return projects


def extract_education(text: str) -> list[str]:
    """
    Extract simple education information.
    """
    education = []

    patterns = [
        r"Bachelor of [^\n]+",
        r"Master of [^\n]+",
        r"B\.?C\.?A\.?",
        r"B\.?Tech\.?",
        r"M\.?C\.?A\.?",
        r"M\.?Tech\.?",
        r"B\.?Sc\.?",
        r"M\.?Sc\.?",
    ]

    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)

        for item in matches:
            item = item.strip()

            if item and item not in education:
                education.append(item)

    return education


def analyze_resume(text: str) -> dict[str, Any]:
    """
    Main Profile Analyzer Agent.

    Takes extracted resume text and returns a structured profile.
    """

    skills = extract_skills(text)
    projects = extract_projects(text)
    education = extract_education(text)

    return {
        "skills": skills,
        "skill_count": len(skills),
        "projects": projects,
        "project_count": len(projects),
        "education": education,
    }