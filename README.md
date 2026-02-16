🎓 Student Data Management & Analytics System
📌 Project Overview
This project is an end-to-end data pipeline designed to manage and analyze academic records. It demonstrates the full lifecycle of a data application: from Relational Database Design in MySQL to Automated Data Generation with Python, and finally, Interactive Visualization using a web dashboard.

🛠️ Tech Stack
Database: MySQL (Relational Schema)

Language: Python 3.x

Data Libraries: Pandas (Analysis), Faker (Mock Data Generation), mysql-connector-python (Database Driver)

Visualization: Streamlit (Web Framework), Plotly (Interactive Charts)

🏗️ Database Architecture
The system uses a Normalized Schema to ensure data integrity and minimize redundancy:

department: Stores college departments and HOD details.

student: Personal details linked to departments.

courses: Academic subjects catalog.

enrollments: Junction table connecting students to their chosen courses.

grades: Tracks performance and marks for every enrollment.

🚀 Key Features
Automated Ingestion: Uses a custom Python script (populate_data.py) and the Faker library to inject 50+ realistic records, eliminating manual entry.

Performance Analytics: SQL-driven insights to find top-performing students and average scores across departments.

Real-time Dashboard: A Streamlit interface that allows users to filter data by department and visualize grade distributions instantly.

📂 File Structure
Plaintext
├── schema.sql           # MySQL table definitions
├── db_config.py         # Database connection configuration
├── populate_data.py     # Script to generate and insert mock data
├── app.py               # Streamlit Dashboard application
└── README.md            # Project documentation
📋 How to Run
Database: Execute the code in schema.sql in your MySQL Workbench.

Setup: Update your credentials in db_config.py.

Populate: Run python populate_data.py to fill the tables.

Launch: Run streamlit run app.py to view the dashboard in your browser.

Author: Sanjeev

Specialization: AI & ML Engineering Student
