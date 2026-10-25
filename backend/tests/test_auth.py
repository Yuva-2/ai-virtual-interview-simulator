def generate_questions_for_resume(profile, role: str, interview_type: str, difficulty: str, total_questions: int, job_description: str | None = None):
    base = [
        f"Tell me about your experience relevant to the {role} role.",
        "Describe a project you worked on and the impact it had on the business or users.",
        "How do you approach debugging a production issue under tight deadlines?",
        "Explain a technical challenge you solved and how you measured success.",
        "Why do you think you are a strong fit for this role and what are your strengths?",
    ]
    if profile and getattr(profile, "skills", None):
        skill_text = getattr(profile, "skills", "")
        if isinstance(skill_text, str):
            base.insert(2, f"How have you applied your skills in {skill_text[:80]} to build or improve systems?")
    if total_questions > len(base):
        total_questions = len(base)
    return base[:total_questions]
