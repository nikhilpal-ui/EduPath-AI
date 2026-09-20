from typing import Any


PRACTICE_LIBRARY: dict[str, dict[str, Any]] = {

    "Statistics": {
        "difficulty": "Beginner",
        "tasks": [
            "Calculate mean, median, mode, variance, and standard deviation for a dataset.",
            "Analyze the distribution of a dataset and identify potential outliers.",
            "Perform a basic hypothesis test and interpret the p-value.",
            "Calculate and interpret correlation between two variables."
        ],
        "project": "Perform an exploratory statistical analysis on a real-world dataset."
    },

    "Data Visualization": {
        "difficulty": "Beginner",
        "tasks": [
            "Create a bar chart for categorical data.",
            "Create a histogram and identify the distribution of a numerical variable.",
            "Create a scatter plot and identify relationships between variables.",
            "Build a small dashboard containing at least three useful visualizations."
        ],
        "project": "Create a data storytelling dashboard from a public dataset."
    },

    "Feature Engineering": {
        "difficulty": "Intermediate",
        "tasks": [
            "Identify and handle missing values in a dataset.",
            "Encode categorical variables using appropriate techniques.",
            "Scale numerical features using StandardScaler or MinMaxScaler.",
            "Create new meaningful features from existing columns.",
            "Compare model performance before and after feature engineering."
        ],
        "project": "Build a complete preprocessing pipeline for a machine learning dataset."
    },

    "Deep Learning": {
        "difficulty": "Intermediate",
        "tasks": [
            "Build a simple neural network for a classification problem.",
            "Experiment with different activation functions.",
            "Train a neural network and monitor training and validation loss.",
            "Explain how backpropagation updates model weights.",
            "Build a basic CNN for image classification."
        ],
        "project": "Build and evaluate a neural network classification project."
    },

    "NLP": {
        "difficulty": "Intermediate",
        "tasks": [
            "Clean and preprocess a text dataset.",
            "Tokenize a collection of text documents.",
            "Convert text into numerical features using TF-IDF.",
            "Build a basic text classification model.",
            "Evaluate the NLP model using precision, recall, and F1-score."
        ],
        "project": "Build a sentiment analysis system using a text dataset."
    },

    "SQL": {
        "difficulty": "Beginner",
        "tasks": [
            "Write SELECT queries with filtering and sorting.",
            "Use GROUP BY and aggregate functions.",
            "Solve problems using INNER JOIN and LEFT JOIN.",
            "Write subqueries for analytical questions.",
            "Use window functions to calculate rankings and running totals."
        ],
        "project": "Analyze a business database and create a SQL-based analytics report."
    },

    "Machine Learning": {
        "difficulty": "Intermediate",
        "tasks": [
            "Build a linear regression model.",
            "Build a classification model using logistic regression.",
            "Train and evaluate a decision tree.",
            "Compare multiple machine learning algorithms.",
            "Evaluate a model using appropriate metrics."
        ],
        "project": "Build an end-to-end machine learning prediction project."
    },

    "Power BI": {
        "difficulty": "Beginner",
        "tasks": [
            "Import and clean a dataset in Power Query.",
            "Create relationships between tables.",
            "Create calculated columns and measures using DAX.",
            "Build an interactive dashboard.",
            "Add filters and slicers for business analysis."
        ],
        "project": "Build an interactive business intelligence dashboard."
    },

    "Excel": {
        "difficulty": "Beginner",
        "tasks": [
            "Clean a raw dataset using Excel functions.",
            "Create Pivot Tables for analysis.",
            "Use lookup functions to combine information.",
            "Create charts from summarized data.",
            "Build an analytical Excel report."
        ],
        "project": "Create an Excel-based business analytics dashboard."
    },

    "React": {
        "difficulty": "Intermediate",
        "tasks": [
            "Create reusable React components.",
            "Manage component state using hooks.",
            "Fetch data from an API.",
            "Create multiple pages using React Router.",
            "Build a responsive React interface."
        ],
        "project": "Build a complete responsive React application."
    }
}


def generate_practice(
    skills: list[str],
    tasks_per_skill: int = 3
) -> list[dict[str, Any]]:

    practice = []

    for skill in skills:

        skill_data = PRACTICE_LIBRARY.get(skill)

        if not skill_data:
            practice.append({
                "skill": skill,
                "difficulty": "Beginner",
                "tasks": [
                    f"Complete a beginner exercise covering {skill}.",
                    f"Apply {skill} to a small dataset or practical problem.",
                    f"Build a small project using {skill}."
                ],
                "mini_project": f"Build a practical project using {skill}."
            })
            continue

        tasks = skill_data["tasks"][:tasks_per_skill]

        practice.append({
            "skill": skill,
            "difficulty": skill_data["difficulty"],
            "tasks": tasks,
            "mini_project": skill_data["project"]
        })

    return practice