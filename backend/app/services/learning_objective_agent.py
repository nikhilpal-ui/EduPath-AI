from typing import Any


LEARNING_OBJECTIVES: dict[str, dict[str, Any]] = {

    "Statistics": {
        "objective": "Build a strong foundation in statistics for data science.",
        "topics": [
            "Descriptive Statistics",
            "Probability",
            "Probability Distributions",
            "Hypothesis Testing",
            "Correlation",
            "Regression"
        ],
        "outcome": "Analyze datasets statistically and interpret statistical results."
    },

    "Data Visualization": {
        "objective": "Learn to communicate data insights using effective visualizations.",
        "topics": [
            "Charts and Graphs",
            "Matplotlib",
            "Seaborn",
            "Choosing the Right Visualization",
            "Dashboard Design",
            "Data Storytelling"
        ],
        "outcome": "Create clear visualizations and communicate meaningful insights."
    },

    "Feature Engineering": {
        "objective": "Transform raw data into useful features for machine learning models.",
        "topics": [
            "Handling Missing Values",
            "Encoding Categorical Variables",
            "Feature Scaling",
            "Feature Selection",
            "Creating New Features",
            "Dimensionality Reduction"
        ],
        "outcome": "Prepare high-quality features that improve machine learning models."
    },

    "Deep Learning": {
        "objective": "Understand neural networks and modern deep learning fundamentals.",
        "topics": [
            "Neural Networks",
            "Activation Functions",
            "Backpropagation",
            "Optimization",
            "CNN",
            "RNN"
        ],
        "outcome": "Build and train basic deep learning models."
    },

    "NLP": {
        "objective": "Learn how machine learning can process and understand human language.",
        "topics": [
            "Text Preprocessing",
            "Tokenization",
            "Stop Words",
            "TF-IDF",
            "Word Embeddings",
            "Text Classification"
        ],
        "outcome": "Build basic NLP pipelines and text classification models."
    },

    "SQL": {
        "objective": "Develop strong SQL skills for querying and analyzing data.",
        "topics": [
            "SELECT Queries",
            "Filtering",
            "GROUP BY",
            "JOINs",
            "Subqueries",
            "Window Functions"
        ],
        "outcome": "Write efficient SQL queries to extract and analyze data."
    },

    "Machine Learning": {
        "objective": "Understand and apply core machine learning algorithms.",
        "topics": [
            "Supervised Learning",
            "Unsupervised Learning",
            "Linear Regression",
            "Logistic Regression",
            "Decision Trees",
            "Model Evaluation"
        ],
        "outcome": "Build, evaluate, and interpret machine learning models."
    },

    "Power BI": {
        "objective": "Create interactive business intelligence dashboards.",
        "topics": [
            "Data Import",
            "Power Query",
            "Data Modeling",
            "DAX",
            "Interactive Dashboards",
            "Dashboard Publishing"
        ],
        "outcome": "Build professional dashboards and communicate business insights."
    },

    "Excel": {
        "objective": "Use Excel effectively for data analysis and reporting.",
        "topics": [
            "Formulas",
            "Functions",
            "Pivot Tables",
            "Data Cleaning",
            "Charts",
            "Lookup Functions"
        ],
        "outcome": "Analyze datasets and create structured analytical reports."
    },

    "React": {
        "objective": "Build modern interactive web applications using React.",
        "topics": [
            "Components",
            "Props",
            "State",
            "Hooks",
            "API Integration",
            "React Router"
        ],
        "outcome": "Build responsive and interactive React applications."
    }
}


def generate_learning_objectives(
    missing_skills: list[str]
) -> list[dict[str, Any]]:

    objectives = []

    for skill in missing_skills:

        objective = LEARNING_OBJECTIVES.get(skill)

        if objective:
            objectives.append({
                "skill": skill,
                "objective": objective["objective"],
                "topics": objective["topics"],
                "expected_outcome": objective["outcome"]
            })

        else:
            objectives.append({
                "skill": skill,
                "objective": f"Develop practical proficiency in {skill}.",
                "topics": [
                    f"{skill} fundamentals",
                    f"{skill} practical applications",
                    f"{skill} project practice"
                ],
                "expected_outcome": f"Apply {skill} effectively in practical projects."
            })

    return objectives