import streamlit as st
import sqlite3
import json
import time
from database import save_result

st.title("Student Portal")

# Fetch latest quiz
conn = sqlite3.connect('classroom.db')
c = conn.cursor()
quiz = c.execute("SELECT topic, questions FROM quizzes ORDER BY id DESC LIMIT 1").fetchone()
conn.close()

if quiz:
    topic, questions_raw = quiz
    questions = json.loads(questions_raw)
    
    st.subheader(f"Today's Quiz: {topic}")
    name = st.text_input("Your Full Name")
    
    if 'start_t' not in st.session_state:
        st.session_state.start_t = time.time()

    responses = []
    for i, q in enumerate(questions):
        ans = st.radio(q['question'], q['options'], key=f"sq_{i}")
        responses.append(ans == q['answer'])

    if st.button("Submit Assessment"):
        duration = round(time.time() - st.session_state.start_t, 2)
        score = (sum(responses) / len(questions)) * 100
        save_result(name, topic, score, duration)
        st.success(f"Done! You scored {score}% in {duration} seconds.")
else:
    st.info("No quiz has been uploaded by the faculty yet.")