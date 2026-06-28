import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
from utils.gemini import analyze_resume

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f7f9fc 0%, #eef2ff 100%);
    }
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        color: #1e293b;
        margin-bottom: 0.2rem;
    }
    .sub-text {
        font-size: 1.05rem;
        color: #475569;
        margin-bottom: 1.5rem;
    }
    .card {
        background: white;
        padding: 1.25rem;
        border-radius: 18px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.06);
        border: 1px solid #e2e8f0;
    }
    .section-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.75rem;
    }
</style>
""", unsafe_allow_html=True)

def extract_text(file):
    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    if file.name.endswith(".docx"):
        doc = Document(file)
        return "\n".join([para.text for para in doc.paragraphs])

    return ""

def render_list(items):
    if not items:
        st.write("No items found.")
        return
    for item in items:
        st.markdown(f"- {item}")

st.markdown('<div class="main-title">🧠 AI Resume Analyzer</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-text">Upload your resume, paste a job description, and get instant AI feedback.</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Upload Resume</div>', unsafe_allow_html=True)
    resume_file = st.file_uploader("Choose a PDF or DOCX file", type=["pdf", "docx"], label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Job Description</div>', unsafe_allow_html=True)
    job_description = st.text_area("Paste the job description here", height=250, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")

analyze_clicked = st.button("✨ Analyze Resume", use_container_width=True)

if analyze_clicked:
    if not resume_file or not job_description:
        st.error("Please upload a resume and paste a job description.")
    else:
        try:
            with st.spinner("Analyzing resume..."):
                resume_text = extract_text(resume_file)
                result = analyze_resume(resume_text, job_description)

            score = int(result.get("match_score", 0))
            score = max(0, min(score, 100))

            st.success("Analysis completed")

            m1, m2, m3 = st.columns(3)
            m1.metric("Match Score", f"{score}%")
            m2.metric("Matched Skills", len(result.get("matched_skills", [])))
            m3.metric("Missing Skills", len(result.get("missing_skills", [])))

            st.progress(score / 100)

            st.markdown("### Overview")
            st.info(result.get("summary", "No summary available."))

            tab1, tab2, tab3, tab4, tab5 = st.tabs(
                ["Matched Skills", "Missing Skills", "Strengths", "Weaknesses", "Suggestions"]
            )

            with tab1:
                render_list(result.get("matched_skills", []))

            with tab2:
                render_list(result.get("missing_skills", []))

            with tab3:
                render_list(result.get("strengths", []))

            with tab4:
                render_list(result.get("weaknesses", []))

            with tab5:
                render_list(result.get("suggestions", []))

            with st.expander("Show extracted resume text"):
                st.text_area("Resume text", resume_text, height=300)

        except Exception as e:
            st.error(f"Something went wrong: {e}")