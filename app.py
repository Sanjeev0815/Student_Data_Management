import streamlit as st
import pandas as pd
import plotly.express as px
from db_config import get_db_connection

st.set_page_config(page_title="EduPath Analytics", layout="wide")
st.title("🎓 Student Performance Analytics Dashboard")

def get_data(query):
    conn = get_db_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter Data")
dept_df = get_data("SELECT dept_name FROM department")
selected_dept = st.sidebar.selectbox("Select Department", dept_df['dept_name'])

# --- MAIN DASHBOARD ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Average Marks by Course")
    avg_marks_query = """
    SELECT c.course_name, AVG(g.marks_obtained) as avg_score
    FROM courses c
    JOIN enrollments e ON c.course_id = e.course_id
    JOIN grades g ON e.enrollment_id = g.enrollment_id
    GROUP BY c.course_name
    """
    df_avg = get_data(avg_marks_query)
    fig = px.bar(df_avg, x='course_name', y='avg_score', color='course_name')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("🏆 Top Performers")
    top_students_query = f"""
    SELECT s.first_name, MAX(g.marks_obtained) as top_score
    FROM student s
    JOIN department d ON s.dept_id = d.dept_id
    JOIN enrollments e ON s.student_id = e.student_id
    JOIN grades g ON e.enrollment_id = g.enrollment_id
    WHERE d.dept_name = '{selected_dept}'
    GROUP BY s.first_name
    ORDER BY top_score DESC LIMIT 5
    """
    df_top = get_data(top_students_query)
    st.table(df_top)

st.subheader("📋 Raw Student Data")
raw_data = get_data("SELECT student_id, first_name, last_name, email FROM student LIMIT 10")
st.dataframe(raw_data, use_container_width=True)