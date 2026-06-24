
def candidate_to_text(candidate):

    profile = candidate["profile"]

    headline = profile.get(
        "headline",
        ""
    )

    summary = profile.get(
        "summary",
        ""
    )

    skills = " ".join(
        skill["name"]
        for skill in candidate["skills"]
    )

    career = " ".join(

        job.get("description", "")

        for job in candidate["career_history"]
    )

    text = f"""
    {headline}
    {summary}
    {skills}
    {career}
    """

    return text