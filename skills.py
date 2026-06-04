skills_list = [
    "python",
    "sql",
    "machine learning",
    "data science",
    "deep learning",
    "power bi",
    "tableau",
    "excel",
    "pandas",
    "numpy",
    "statistics",
    "tensorflow",
    "opencv",
    "scikit-learn",
    "data visualization"
]

def extract_skills(text):

    found_skills = []

    text = text.lower()

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills