import streamlit as st
import re
from collections import Counter
import PyPDF2
# ------------------ Stopwords ------------------
STOPWORDS = {
    "the", "and", "is", "in", "to", "of", "for",
    "with", "a", "an", "on", "at", "by", "this",
    "that", "from", "as", "it", "are"
}
# ------------------ Text Processing ------------------
def extract_keywords(text):
    words = re.findall(r'\w+', text.lower())
    filtered = [word for word in words if word not in STOPWORDS and len(word) > 2]
    return Counter(filtered)
def analyze_resume(job_desc, resume):
    job_keywords = extract_keywords(job_desc)
    resume_keywords = extract_keywords(resume)
    job_unique = set(job_keywords.keys())
    resume_unique = set(resume_keywords.keys())
    matched = sorted(job_unique.intersection(resume_unique))
    missing = sorted(job_unique.difference(resume_unique))
    match_percentage = (len(matched) / len(job_unique)) * 100 if job_unique else 0
    return matched, missing, round(match_percentage, 2)
# ------------------ PDF Reader ------------------
def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text
# ------------------ Streamlit UI ------------------
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
st.title("AI Resume Keyword Analyzer with PDF Support")
st.write("Upload your resume as PDF or paste text to analyze keyword matching with a job description.")
job_description = st.text_area("Enter Job Description", height=200)
resume_option = st.radio(
    "Choose Resume Input Method:",
    ("Paste Resume Text", "Upload Resume PDF")
)
resume_text = ""
if resume_option == "Paste Resume Text":
    resume_text = st.text_area("Enter Resume Text", height=200)
else:
    uploaded_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])
    if uploaded_file is not None:
        resume_text = extract_text_from_pdf(uploaded_file)
        st.success("PDF uploaded and text extracted successfully.")
if st.button("Analyze Resume"):
    if job_description.strip() and resume_text.strip():
        matched, missing, percentage = analyze_resume(job_description, resume_text)
        st.subheader("Analysis Result")
        st.write(f"Match Percentage: {percentage}%")
        st.subheader("Matched Keywords")
        if matched:
            st.success(", ".join(matched))
        else:
            st.write("No matched keywords found.")
        st.subheader("Missing Keywords")
        if missing:
            st.error(", ".join(missing))
        else:
            st.write("No missing keywords.")
    else:
        st.warning("Please provide both Job Description and Resume.")
