import streamlit as st
import joblib

st.set_page_config(
    page_title="Fake Job Posting Detector",
    page_icon="🕵️",
    layout="centered"
)

model = joblib.load("fake_job_detector.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.title("🕵️ Fake Job Posting Detector")

st.markdown("""
This application predicts whether a job posting is **Genuine** or **Fake**
using a Machine Learning model trained on thousands of job advertisements.
""")

job_text = st.text_area(
    "Paste Job Description",
    height=250,
    placeholder="Paste the complete job description here..."
)

if st.button("🔍 Analyze Job"):

    if job_text.strip() == "":
        st.warning("Please enter a job description.")
    else:

        vector = vectorizer.transform([job_text])

        prediction = model.predict(vector)
        probability = model.predict_proba(vector)

        confidence = probability.max() * 100

        st.divider()

        if prediction[0] == 1:
            st.error("❌ Fake Job Posting")
        else:
            st.success("✅ Genuine Job Posting")

        st.metric("Confidence", f"{confidence:.2f}%")