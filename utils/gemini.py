import os
import json
import re
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

def _extract_json(text: str) -> dict:
    text = text.strip()
    text = re.sub(r"^```json\s*", "", text)
    text = re.sub(r"^```\s*", "", text)
    text = re.sub(r"\s*```$", "", text)

    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        text = match.group(0)

    return json.loads(text)

def analyze_resume(resume_text, job_description):
    prompt = f"""
You are an expert recruiter.

Compare the resume with the job description and return ONLY valid JSON
with this exact structure:

{{
  "match_score": 0,
  "summary": "short summary",
  "matched_skills": ["skill 1", "skill 2"],
  "missing_skills": ["skill 1", "skill 2"],
  "strengths": ["strength 1", "strength 2"],
  "weaknesses": ["weakness 1", "weakness 2"],
  "suggestions": ["suggestion 1", "suggestion 2"]
}}

Rules:
- match_score must be an integer from 0 to 100
- all list values must be arrays of short bullet items
- do not add any extra text outside JSON

Resume:
{resume_text}

Job Description:
{job_description}
"""

    response = client.models.generate_content(
        # model="gemini-3.5-flash",
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return _extract_json(response.text)