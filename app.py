import streamlit as st
from database import init_db

st.set_page_config(page_title="EduQuiz AI", layout="wide")
init_db()

st.title("🚀 Welcome to EduQuiz AI")
st.markdown("""
### The Future of Instant Classroom Assessment
Use the sidebar to navigate:
1. **Faculty Dashboard**: Generate a quiz using AI and view student analytics.
2. **Student Portal**: Take the quiz assigned for today.
""")