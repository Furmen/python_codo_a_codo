from flask import Flask, request, flash, redirect, url_for
import database.db
import validations.repeatEmail
import usecases.add
import usecases.delete
import usecases.read
import usecases.update

app = Flask(__name__)

mysql = database.db.configDB(app)
checkEmail = validations.repeatEmail
addStudentUseCase = usecases.add
updateStudentUseCase = usecases.update
deleteStudentUseCase = usecases.delete
readStudentUseCase = usecases.read


@app.route('/')
def Index():
    return readStudentUseCase.readStudents()


@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    if deleteStudentUseCase.deleteStudent(id_data):
        return redirect(url_for('Index'))
    else:
        flash("Error: Surgión un error en la eliminación del alumno.")
        return redirect(url_for('Index'))


@app.route('/insert', methods=['POST'])
def insert():
    if addStudentUseCase.addStudent(request):
        flash("Los datos fueron ingresados correctamente")
        return redirect(url_for('Index'))
    else:
        flash("Error: El email ya se encuentra registrado. Por favor cambielo.")
        return redirect(url_for('Index'))


@app.route('/update', methods=['POST', 'GET'])
def update():
    if updateStudentUseCase.updateStudent(request):
        flash("El registro fue actualizado correctamente")
        return redirect(url_for('Index'))
    else:
        flash("Error: El email ya se encuentra registrado. Por favor cambielo.")
        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)
