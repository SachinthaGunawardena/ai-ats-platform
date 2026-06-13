from app.services.resume_intelligence import (
    build_resume_profile
)


def test_profile_build():

    text = """
    John Smith

    john@gmail.com

    +1 555 123 4567

    Python Developer

    5 years experience

    Skills:
    Python
    FastAPI
    PostgreSQL

    Bachelor of Computer Science
    """

    profile = build_resume_profile(text)

    assert profile.email == "john@gmail.com"

    assert "python" in profile.skills

    assert profile.experience_years == 5