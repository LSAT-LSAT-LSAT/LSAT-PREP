
import streamlit as st
import json
import datetime
import pandas as pd
import altair as alt

# ---- Initialization ----
st.set_page_config(page_title="LSAT 177+ Study App", layout="wide")
st.title("🧠 LSAT 177+ Study Tracker")

# ---- Sidebar Inputs ----
st.sidebar.header("📅 Daily Checklist")
daily_tasks = {
    "Core Skills Drill": False,
    "Timed Section Practice": False,
    "Blind Review": False,
    "Mistake Log Update": False
}

today = str(datetime.date.today())

# Load saved progress if exists
def load_progress():
    try:
        with open("progress.json", "r") as f:
            return json.load(f)
    except:
        return {}

progress = load_progress()

# Initialize today if not already present
if today not in progress:
    progress[today] = daily_tasks.copy()

# Sidebar Checkboxes
for task in daily_tasks:
    checked = st.sidebar.checkbox(task, value=progress[today][task])
    progress[today][task] = checked

# Save progress
with open("progress.json", "w") as f:
    json.dump(progress, f, indent=2)

# ---- Main View ----
st.subheader(f"📊 Progress for {today}")
st.write(progress[today])

# Score Logging
st.sidebar.header("📈 Score Logging")
if "scores" not in progress:
    progress["scores"] = []

raw = st.sidebar.number_input("Raw Score", min_value=0, max_value=76)
scaled = st.sidebar.number_input("Scaled Score", min_value=120, max_value=180)
pt_number = st.sidebar.text_input("PrepTest #")
note = st.sidebar.text_input("Notes")

if st.sidebar.button("Log Score"):
    score_entry = {
        "date": today,
        "pt": pt_number,
        "raw": raw,
        "scaled": scaled,
        "notes": note
    }
    progress["scores"].append(score_entry)
    with open("progress.json", "w") as f:
        json.dump(progress, f, indent=2)
    st.sidebar.success("Logged!")

# Score Chart
if progress.get("scores"):
    df_scores = pd.DataFrame(progress["scores"])
    if not df_scores.empty:
        st.subheader("📈 Score History")
        st.altair_chart(alt.Chart(df_scores).mark_line(point=True).encode(
            x="date:T",
            y="scaled:Q",
            tooltip=["date", "pt", "raw", "scaled", "notes"]
        ).properties(height=400), use_container_width=True)

# TODO: Notion + Google Sheets Integration
st.markdown("🔧 *Notion and Google Sheets integration coming next...*")
