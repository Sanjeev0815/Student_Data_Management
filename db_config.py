import mysql.connector
def get_db_connection():
    try:
        connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sanjeev@123",
            database="university_db"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None