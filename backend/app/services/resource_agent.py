from typing import Any


RESOURCE_LIBRARY: dict[str, list[dict[str, Any]]] = {

    "Statistics": [
        {
            "title": "Statistics Fundamentals",
            "type": "Course",
            "level": "Beginner",
            "platform": "Khan Academy",
            "url": "https://www.khanacademy.org/math/statistics-probability",
            "duration": "8-12 hours"
        },
        {
            "title": "Statistics for Data Science",
            "type": "Learning Path",
            "level": "Intermediate",
            "platform": "Coursera",
            "url": "https://www.coursera.org/",
            "duration": "15-20 hours"
        }
    ],

    "Data Visualization": [
        {
            "title": "Matplotlib Documentation",
            "type": "Documentation",
            "level": "Beginner",
            "platform": "Matplotlib",
            "url": "https://matplotlib.org/stable/",
            "duration": "4-6 hours"
        },
        {
            "title": "Seaborn Documentation",
            "type": "Documentation",
            "level": "Beginner",
            "platform": "Seaborn",
            "url": "https://seaborn.pydata.org/",
            "duration": "3-5 hours"
        }
    ],

    "Feature Engineering": [
        {
            "title": "Feature Engineering",
            "type": "Course",
            "level": "Intermediate",
            "platform": "Kaggle",
            "url": "https://www.kaggle.com/learn",
            "duration": "4-6 hours"
        },
        {
            "title": "Scikit-learn Preprocessing",
            "type": "Documentation",
            "level": "Intermediate",
            "platform": "Scikit-learn",
            "url": "https://scikit-learn.org/stable/modules/preprocessing.html",
            "duration": "3-5 hours"
        }
    ],

    "Deep Learning": [
        {
            "title": "Intro to Deep Learning",
            "type": "Course",
            "level": "Intermediate",
            "platform": "Kaggle",
            "url": "https://www.kaggle.com/learn/intro-to-deep-learning",
            "duration": "5-7 hours"
        },
        {
            "title": "Deep Learning Specialization",
            "type": "Specialization",
            "level": "Intermediate",
            "platform": "Coursera",
            "url": "https://www.coursera.org/specializations/deep-learning",
            "duration": "40+ hours"
        }
    ],

    "NLP": [
        {
            "title": "Natural Language Processing",
            "type": "Course",
            "level": "Intermediate",
            "platform": "Kaggle",
            "url": "https://www.kaggle.com/learn",
            "duration": "5-8 hours"
        },
        {
            "title": "Hugging Face NLP Course",
            "type": "Course",
            "level": "Intermediate",
            "platform": "Hugging Face",
            "url": "https://huggingface.co/learn/nlp-course",
            "duration": "15-25 hours"
        }
    ],

    "SQL": [
        {
            "title": "SQL Tutorial",
            "type": "Practice",
            "level": "Beginner",
            "platform": "W3Schools",
            "url": "https://www.w3schools.com/sql/",
            "duration": "6-10 hours"
        },
        {
            "title": "SQL Practice",
            "type": "Practice",
            "level": "Intermediate",
            "platform": "HackerRank",
            "url": "https://www.hackerrank.com/domains/sql",
            "duration": "10-15 hours"
        }
    ],

    "Machine Learning": [
        {
            "title": "Intro to Machine Learning",
            "type": "Course",
            "level": "Beginner",
            "platform": "Kaggle",
            "url": "https://www.kaggle.com/learn/intro-to-machine-learning",
            "duration": "3-5 hours"
        },
        {
            "title": "Machine Learning Specialization",
            "type": "Specialization",
            "level": "Intermediate",
            "platform": "Coursera",
            "url": "https://www.coursera.org/specializations/machine-learning-introduction",
            "duration": "30-40 hours"
        }
    ],

    "Power BI": [
        {
            "title": "Power BI Learning",
            "type": "Learning Path",
            "level": "Beginner",
            "platform": "Microsoft Learn",
            "url": "https://learn.microsoft.com/training/powerplatform/power-bi/",
            "duration": "8-12 hours"
        }
    ],

    "Excel": [
        {
            "title": "Excel Training",
            "type": "Course",
            "level": "Beginner",
            "platform": "Microsoft",
            "url": "https://support.microsoft.com/excel",
            "duration": "6-10 hours"
        }
    ],

    "React": [
        {
            "title": "React Documentation",
            "type": "Documentation",
            "level": "Beginner",
            "platform": "React",
            "url": "https://react.dev/",
            "duration": "8-12 hours"
        }
    ]
}


def recommend_resources(
    missing_skills: list[str],
    level: str = "Beginner"
) -> list[dict[str, Any]]:

    recommendations = []

    for skill in missing_skills:

        resources = RESOURCE_LIBRARY.get(skill, [])

        if not resources:
            recommendations.append({
                "skill": skill,
                "resources": []
            })
            continue

        filtered_resources = [
            resource
            for resource in resources
            if resource["level"] == level
        ]

        if not filtered_resources:
            filtered_resources = resources

        recommendations.append({
            "skill": skill,
            "resources": filtered_resources
        })

    return recommendations