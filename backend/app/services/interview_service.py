import re
from typing import List

from pypdf import PdfReader

from app.schemas.models import ResumeExtracted


def parse_resume_text(pdf_bytes: bytes) -> str:
    try:
        from io import BytesIO
        reader = PdfReader(BytesIO(pdf_bytes))
        texts = []
        for page in reader.pages:
            texts.append(page.extract_text() or "")
        return "\n".join(texts)
    except Exception:
        return ""


def extract_resume_profile(text: str) -> ResumeExtracted:
    normalized = text or ""
    email_match = re.search(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", normalized, re.I)
    phone_match = re.search(r"(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?)\d{3}[-.\s]?\d{4}", normalized)
    name_match = re.search(r"^\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)", normalized, re.M)

    skills = [s.strip() for s in re.findall(r"(Python|Java|JavaScript|TypeScript|React|FastAPI|SQL|PostgreSQL|Machine Learning|Deep Learning|AWS|Docker|Git|Node\.js|C\+\+|C#)", normalized, re.I)]
    if not skills:
        skills = ["Communication", "Problem Solving", "Teamwork"]

    education = re.findall(r"(?:B\.Tech|M\.Tech|B\.E|M\.E|B\.Sc|M\.Sc|Bachelor|Master|Diploma)[^.]*[^\n]+", normalized, re.I)
    experience = re.findall(r"(?:Intern|Engineer|Developer|Analyst|Manager)[^.]*", normalized, re.I)[:5]
    projects = re.findall(r"(?:Project|Projects|Built|Developed)[^.]*", normalized, re.I)[:5]
    certifications = re.findall(r"(?:AWS|Google|Microsoft|Oracle|Certified|CCNA|PMP)[^.]*", normalized, re.I)[:5]

    profile = ResumeExtracted(
        full_name=name_match.group(1) if name_match else "Candidate",
        email=email_match.group(0) if email_match else None,
        phone=phone_match.group(0).strip() if phone_match else None,
        summary=(normalized[:250].strip() if normalized else "Candidate profile extracted from resume."),
        skills=skills,
        education=education[:5],
        experience=experience[:5],
        projects=projects[:5],
        certifications=certifications[:5],
        confidence_score=0.9,
    )
    return profile
