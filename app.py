import streamlit as st
import pdfplumber
import matplotlib.pyplot as plt
from skills import extract_skills

st.set_page_config(
    page_title="Placement Readiness Analyzer",
    page_icon="📊"
)

st.title("📊 Placement Readiness Analyzer")

st.write(
    "Upload your resume and compare it against your target role and job description."
)

role = st.selectbox(
    "Select Target Role",
    [
        "Data Analyst",
        "Data Scientist",
        "ML Engineer"
    ]
)

job_description = st.text_area(
    "Paste Job Description Here",
    height=200
)

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

    st.subheader("📄 Resume Text")

    st.text_area(
        "Extracted Resume Content",
        text,
        height=250
    )

    skills = extract_skills(text)

    st.subheader("🛠 Skills Detected")

    if skills:
        st.write(skills)
    else:
        st.warning("No skills detected.")

    # Role Requirements

    if role == "Data Analyst":

        required_skills = [
            "sql",
            "excel",
            "power bi",
            "tableau",
            "statistics",
            "python"
        ]

    elif role == "Data Scientist":

        required_skills = [
            "python",
            "sql",
            "pandas",
            "numpy",
            "machine learning",
            "statistics",
            "data science"
        ]

    else:

        required_skills = [
            "python",
            "machine learning",
            "deep learning",
            "tensorflow",
            "numpy",
            "opencv"
        ]

    # Placement Readiness Score

    matched = len(
        set(skills) & set(required_skills)
    )

    score = int(
        (matched / len(required_skills)) * 100
    )

    st.subheader("🎯 Placement Readiness Score")

    st.progress(score)

    st.success(f"Score: {score}/100")

    # ATS Score

    ats_score = score + 10

    if ats_score > 100:
        ats_score = 100

    st.subheader("📄 ATS Score")

    st.progress(ats_score)

    st.success(f"ATS Score: {ats_score}/100")

    # Missing Skills

    missing_skills = list(
        set(required_skills) - set(skills)
    )

    st.subheader("📌 Missing Skills")

    if missing_skills:

        for skill in missing_skills:
            st.write("•", skill)

    else:

        st.success(
            "All required skills found!"
        )

    # Job Description Matching

    if job_description:

        st.subheader("📋 Job Description Match")

        jd_text = job_description.lower()

        matched_keywords = []

        for skill in skills:

            if skill in jd_text:
                matched_keywords.append(skill)

        if len(skills) > 0:

            jd_score = int(
                (len(matched_keywords) / len(skills)) * 100
            )

        else:

            jd_score = 0

        st.progress(jd_score)

        st.success(
            f"Job Description Match Score: {jd_score}%"
        )

        st.write("✅ Matching Skills")

        st.write(matched_keywords)

    # Learning Roadmap

    st.subheader("📚 Learning Roadmap")

    for skill in missing_skills:
        st.write(f"Learn {skill}")

    # Skill Chart

    st.subheader("📊 Skill Match Chart")

    matched_count = len(
        set(skills) & set(required_skills)
    )

    missing_count = len(missing_skills)

    fig, ax = plt.subplots()

    ax.bar(
        ["Matched", "Missing"],
        [matched_count, missing_count]
    )

    st.pyplot(fig)

    # Feedback

    st.subheader("📝 Resume Feedback")

    if score >= 80:

        st.success(
            "Excellent profile for this role."
        )

    elif score >= 60:

        st.warning(
            "Good profile. Improve a few missing skills."
        )

    else:

        st.error(
            "Significant improvement needed."
        )

    # Projects

    st.subheader("🚀 Suggested Projects")

    if role == "Data Analyst":

        st.write("• Customer Churn Analysis")
        st.write("• Sales Dashboard")
        st.write("• SQL Analytics")

    elif role == "Data Scientist":

        st.write("• Fraud Detection")
        st.write("• House Price Prediction")
        st.write("• Customer Segmentation")

    else:

        st.write("• Deepfake Detection")
        st.write("• Face Recognition")
        st.write("• Object Detection")

    # Certifications

    st.subheader("🎓 Recommended Certifications")

    if role == "Data Analyst":

        st.write("• Google Data Analytics")
        st.write("• Power BI Certification")

    elif role == "Data Scientist":

        st.write("• IBM Data Science")
        st.write("• Machine Learning Specialization")

    else:

        st.write("• TensorFlow Developer")
        st.write("• Deep Learning Specialization")