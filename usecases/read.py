from flask import render_template
import database.db

mysql = database.db.getConnectionDB()

def readStudents():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM students order by id")
    data = cur.fetchall()
    cur.close()
    return render_template('index2.html', students=data)