import re

from app.schemas.resume_profile import ResumeProfile

def extract_email(text: str):
    match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    return match.group(0) if match else None

def extract_phone(text: str):
    match = re.search(
        r"(\+?\d[\d\s\-]{8,15})",
        text
    )

    return match.group(0) if match else None

SKILLS = [
    "python",
    "java",
    "javascript",
    "typescript",
    "react",
    "node",
    "fastapi",
    "django",
    "flask",
    "postgresql",
    "mysql",
    "mongodb",
    "docker",
    "kubernetes",
    "aws",
    "azure",
]

def extract_skills(text: str):
    text_lower = text.lower()

    found = []

    for skill in SKILLS:
        if skill in text_lower:
            found.append(skill)

    return list(set(found))

def extract_experience_years(text: str):
    match = re.search(
        r"(\d+)\+?\s+years",
        text.lower()
    )

    if match:
        return int(match.group(1))

    return None

EDUCATION_KEYWORDS = [
    "bachelor",
    "master",
    "phd",
    "computer science",
    "software engineering",
]

def extract_education(text: str):
    text_lower = text.lower()

    found = []

    for item in EDUCATION_KEYWORDS:
        if item in text_lower:
            found.append(item)

    return found


def build_resume_profile(text: str):

    profile = ResumeProfile(
        email=extract_email(text),
        phone=extract_phone(text),
        skills=extract_skills(text),
        education=extract_education(text),
        experience_years=extract_experience_years(text),
    )

    return profile