import database.db

mysql = database.db.getConnectionDB()

def deleteStudent(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return True