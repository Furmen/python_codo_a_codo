import database.db
import validations.repeatEmail

mysql = database.db.getConnectionDB()
checkEmail = validations.repeatEmail


def addStudent(request):
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        image = request.form['hdnImageNew']

        if checkEmail.validateStudentData(email):
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO students (name, email, phone, image) VALUES (%s, %s, %s, %s)",
                        (name, email, phone, image))
            mysql.connection.commit()
            return True
    return False
