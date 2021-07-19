import database.db

mysql = database.db.getConnectionDB()

def validateStudentData(emailStudent):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students WHERE email=%s", (emailStudent,))
    data = cur.fetchall()
    cur.close()
    
    if data:
        return False
    
    return True