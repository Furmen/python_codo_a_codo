from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = 'many random bytes'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)

def validateStudentData(emailStudent):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students WHERE email=%s", (emailStudent,))
    data = cur.fetchall()
    cur.close()
    
    if data:
        return False
    
    return True

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM students order by id")
    data = cur.fetchall()
    cur.close()
    return render_template('index2.html', students=data)

@app.route('/insert', methods=['POST'])
def insert():

    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        image = request.form['hdnImageNew']

        if validateStudentData(email):        
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO students (name, email, phone, image) VALUES (%s, %s, %s, %s)", (name, email, phone, image))
            mysql.connection.commit()
            flash("Los datos fueron ingresados correctamente")
            return redirect(url_for('Index'))
        
    flash("Error: El email ya se encuentra registrado. Por favor cambielo.")
    return redirect(url_for('Index'))

@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    flash("El registro fue eliminado correctamente")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))

@app.route('/update', methods=['POST', 'GET'])
def update():

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
        flash("El registro fue actualizado correctamente")
        mysql.connection.commit()
        return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True)
