from db_config import get_db_connection
def test():
    conn=get_db_connection()
    if conn and conn.is_connected():
        print("Connected")
        conn.close()
    else:
        print("Failed")
if __name__=="__main__":
    test()