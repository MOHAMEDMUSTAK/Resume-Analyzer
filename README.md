# AI Resume Keyword Analyzer (Web App with PDF Support)
## Overview
A web-based AI-powered Resume Keyword Analyzer built using Python and Streamlit. This application evaluates how well a resume matches a job description by extracting meaningful keywords, removing stopwords, and calculating a match percentage. It supports both direct text input and PDF resume uploads, simulating a simplified Applicant Tracking System (ATS).
## Features
- Keyword extraction using Natural Language Processing techniques
- Stopword filtering for improved accuracy
- Resume-to-job match percentage calculation
- Identification of matched and missing keywords
- PDF resume upload and automatic text extraction
- Interactive web interface
## Tech Stack
- Python 3
- Streamlit
- PyPDF2
- Regular Expressions
- Collections (Counter)
## How It Works
The system extracts keywords from both the job description and resume text. After removing common stopwords, it compares unique keyword sets to determine overlap. The match percentage is calculated based on matched keywords relative to total job description keywords.
## How to Run
1. Install dependencies:
   pip install -r requirements.txt
2. Start the application:
   streamlit run app.py
3. Open the local browser link provided.
## Use Case
- Resume optimization for ATS systems
- Job seekers improving keyword alignment
- Demonstration of NLP-based text analysis
- Educational project for AI and text processing
## Future Improvements
- TF-IDF weighting
- Cosine similarity scoring
- Skill prioritization
- Section-based resume analysis
- Cloud deployment
## Author
Mohamed Mustak M