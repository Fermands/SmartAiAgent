import json
with open("summer_school_2025.json", "r", encoding="utf-8") as f:
    DATA = json.load(f)
def get_answer(question: str) -> str:
    q = question.lower()
    if "introduction" in q:
        return f"🏕️ *Introduction:*\n{DATA['introduction']}"
    elif "goal" in q:
        goals = "\n".join(f"- {g}" for g in DATA["goals"])
        return f"🎯 *Goals of the Summer School:*\n{goals}"
    elif "milestone" in q or "timeline" in q:
        milestones = "\n".join(f"🗓️ *{k}*: {v}" for k, v in DATA["milestones"].items())
        return f"📅 *Project Milestones:*\n{milestones}"
    elif "eligibility" in q or "who can apply" in q:
        return f"✅ *Eligibility:*\n{DATA['student_selection']['eligibility']}"
    elif "selection" in q or "apply" in q or "admission" in q:
        stages = "\n".join(f"{i+1}. {stage}" for i, stage in enumerate(DATA["student_selection"]["stages"]))
        timeline = DATA["student_selection"]["timeline"]
        return f"📝 *Selection Stages:*\n{stages}\n\n🗓️ *Timeline:* {timeline}"
    elif "academic" in q or "topic" in q or "program" in q:
        ap = DATA["academic_program"]
        focus_areas = "\n".join(f"- {area}" for area in ap["focus_areas"])
        return (
            f"📚 *Academic Program*\n\n"
            f"🧠 *Focus Areas:*\n{focus_areas}\n\n"
            f"🗓️ *Timeline:* {ap['timeline']}\n"
            f"🧩 *Structure:* {ap['structure']}"
        )
    elif "social" in q or "game" in q or "activity" in q:
        highlights = "\n".join(f"- {h}" for h in DATA["social_activities"]["highlights"])
        return (
            f"🎉 *Social Activities:*\n{highlights}\n\n"
            f"🗓️ *When:* {DATA['social_activities']['timeline']}"
        )
    elif "budget" in q or "cost" in q or "price" in q:
        b = DATA["budgeting"]
        return (
            f"💰 *Budget Info:*\n"
            f"- Estimated cost per participant: ${b['estimated_cost_per_participant']}\n"
            f"- Maximum participants: {b['max_participants']}\n"
            f"❗ {b['note']}"
        )
    elif "contact" in q or "email" in q or "phone" in q:
        c = DATA["contacts"]
        return (
            f"📞 *Phone Numbers:*\n"
            f"- School: {c['school_phone']}\n"
            f"- University: {c['university_phone']}\n\n"
            f"📧 *Emails:*\n"
            f"- School: {c['school_email']}\n"
            f"- University: {c['university_email']}\n\n"
            f"🔗 *Links:*\n"
            f"- Website: {c['website']}\n"
            f"- Telegram: {c['telegram']}\n"
            f"- YouTube: {c['youtube']}\n"
            f"- Instagram: {c['instagram']}"
        )

    elif "link" in q or "website" in q:
        return f"🌐 *Official Website:*\n{DATA['contacts']['website']}"

    elif "initiator" in q or "organizer" in q or "founder" in q:
        initiator = DATA["main_initiator"]
        support = "\n".join(f"- {s}" for s in initiator["support"])
        founders = "\n".join(f"- {f}" for f in initiator["founders"])
        return (
            f"🏫 *Main Initiator:* {initiator['name']}\n\n"
            f"🤝 *Support Provided:*\n{support}\n\n"
            f"👥 *Founders:*\n{founders}"
        )

    elif "statistic" in q or "result" in q or "data" in q:
        return f"📊 *Statistics Website:* {DATA['statistics_website']}"

    elif "cohort" in q or "previous" in q or "past" in q:
        cohorts = "\n".join(f"- {c}" for c in DATA["cohorts"])
        return f"📖 *Previous Cohorts:*\n{cohorts}"

    return "🤔 Sorry, I can only answer questions about the Summer School 2025."
