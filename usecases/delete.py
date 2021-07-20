from flask import redirect, url_for, flash
import database.db

mysql = database.db.getConnectionDB()

def deleteStudent(id_data):
    flash("El registro fue eliminado correctamente")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return True