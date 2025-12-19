import streamlit as st
import json
from openai import OpenAI
from database import save_quiz, get_results
import plotly.express as px

client = OpenAI(api_key="YOUR_OPENAI_KEY")

st.title("Faculty Dashboard")

# --- Generation Section ---
with st.expander("Create New Quiz", expanded=True):
    sub = st.text_input("Subject")
    top = st.text_input("Topic")
    cont = st.text_area("Lesson Content")
    
    if st.button("Generate & Save Quiz"):
        prompt = f"Create a 3-question MCQ quiz on {top} based on: {cont}. Return ONLY valid JSON list."
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role":"user","content":prompt}])
        save_quiz(sub, top, cont, response.choices[0].message.content)
        st.success(f"Quiz for {top} is now live!")

# --- Analytics Section ---
st.divider()
st.header("Class Analytics")
target_topic = st.text_input("Enter Topic to Analyze", value=top)

if target_topic:
    df = get_results(target_topic)
    if not df.empty:
        avg = df['score'].mean()
        st.metric("Class Average", f"{avg}%")
        
        if avg < 60:
            st.error(f"⚠️ Warning: Average is {avg}%. Recommendation: Repeat the topic '{target_topic}'.")
        
        fig = px.bar(df, x="student_name", y="score", color="score", title="Student Performance")
        st.plotly_chart(fig)
    else:
        st.info("No results found for this topic yet.")