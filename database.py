import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect('classroom.db')
    c = conn.cursor()

    # Table for Quizzes
    c.execute('''CREATE TABLE IF NOT EXISTS quizzes 
                 (id INTEGER PRIMARY KEY, subject TEXT, topic TEXT, content TEXT, questions TEXT)''')
    
    # Table for Student Results
    c.execute('''CREATE TABLE IF NOT EXISTS results 
                 (id INTEGER PRIMARY KEY, student_name TEXT, topic TEXT, score REAL, time_spent REAL)''')
    conn.commit()
    conn.close()

def save_quiz(subject, topic, content, questions_json):
    conn = sqlite3.connect('classroom.db')
    c = conn.cursor()
    c.execute("INSERT INTO quizzes (subject, topic, content, questions) VALUES (?, ?, ?, ?)",
              (subject, topic, content, questions_json))
    conn.commit()
    conn.close()

def save_result(name, topic, score, time_spent):
    conn = sqlite3.connect('classroom.db')
    c = conn.cursor()
    c.execute("INSERT INTO results (student_name, topic, score, time_spent) VALUES (?, ?, ?, ?)",
              (name, topic, score, time_spent))
    conn.commit()
    conn.close()

def get_results(topic):
    conn = sqlite3.connect('classroom.db')
    df = pd.read_sql_query("SELECT * FROM results WHERE topic=?", conn, params=(topic,))
    conn.close()
    return df