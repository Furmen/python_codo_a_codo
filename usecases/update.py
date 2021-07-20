import database.db
import validations.repeatEmail

mysql = database.db.getConnectionDB()
checkEmail = validations.repeatEmail


def updateStudent(request):
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        image = request.form['hdnImageEdit']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE students
            SET name=%s, email=%s, phone=%s, image=%s
            WHERE id=%s
            """, (name, email, phone, image, id_data))
        mysql.connection.commit()
        return True

    return False
