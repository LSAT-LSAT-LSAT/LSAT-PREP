
import streamlit as st
import json
import random

# Load drill data
with open("logic_drills.json", "r") as f:
    drills = json.load(f)

# Select random drill or allow selection
if "current_drill" not in st.session_state:
    st.session_state.current_drill = random.choice(drills)

drill = st.session_state.current_drill

st.title("🧠 Logic Drill Mode")
st.subheader(f"Type: {drill['type']}")
st.write(drill["question"])

user_answer = st.radio("Choose your answer:", drill["choices"], index=None)

if st.button("Submit Answer"):
    correct = drill["answer"]
    if drill["choices"].index(user_answer) == correct:
        st.success("✅ Correct!")
    else:
        st.error("❌ Incorrect.")
    st.markdown(f"**Explanation:** {drill['explanation']}")

    if st.button("Next Question"):
        st.session_state.current_drill = random.choice(drills)
        st.experimental_rerun()
