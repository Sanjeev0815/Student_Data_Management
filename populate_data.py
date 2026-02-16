import random
from faker import Faker
from db_config import get_db_connection

fake = Faker()
conn = get_db_connection()
cursor = conn.cursor()

def populate():
    try:
        
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        cursor.execute("TRUNCATE TABLE grades")
        cursor.execute("TRUNCATE TABLE enrollments")
        cursor.execute("TRUNCATE TABLE student")
        cursor.execute("TRUNCATE TABLE courses")
        cursor.execute("TRUNCATE TABLE department")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

        # 1. Departments
        depts = [('AI-ML', 'Dr. Sharma'), ('CSE', 'Dr. Reddy'), ('ECE', 'Dr. Verma')]
        #
        cursor.executemany("INSERT INTO department (dept_name, hod_name) VALUES (%s, %s)", depts)

        # 2. Students
        for _ in range(50):
            fname = fake.first_name()
            lname = fake.last_name()
            email = fake.unique.email()
            dept_id = random.randint(1, 3)
            cursor.execute("INSERT INTO student (first_name, last_name, email, dept_id) VALUES (%s, %s, %s, %s)", 
                           (fname, lname, email, dept_id))
            
        # 3. Courses 
        courses = [('Machine Learning', 4, 1), ('Data Structures', 3, 2), ('Signals', 3, 3)]
        cursor.executemany("INSERT INTO courses (course_name, credits, dept_id) VALUES (%s, %s, %s)", courses)

        # 4. Enrollments and Grades
        cursor.execute("SELECT student_id FROM student") 
        student_ids = [row[0] for row in cursor.fetchall()]
        
        for s_id in student_ids:
            # Enroll each student in 2 random courses
            for c_id in random.sample([1, 2, 3], 2): 
                cursor.execute("INSERT INTO enrollments (student_id, course_id, semester) VALUES (%s, %s, %s)", 
                               (s_id, c_id, 'Sem 2'))
                e_id = cursor.lastrowid
                
                marks = random.randint(45, 98)
                letter = 'A' if marks > 90 else 'B' if marks > 75 else 'C'
                cursor.execute("INSERT INTO grades (enrollment_id, marks_obtained, grade_letter) VALUES (%s, %s, %s)", 
                               (e_id, marks, letter))
        
        conn.commit()
        print( "Database Populated Successfully with 50 Students!")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    populate()