from flask import Flask, request, flash, redirect, url_for

import usecases.add
import usecases.delete
import usecases.read
import usecases.update

app = Flask(__name__)

addStudentUseCase = usecases.add
updateStudentUseCase = usecases.update
deleteStudentUseCase = usecases.delete
readStudentUseCase = usecases.read
message = ""


@app.route('/')
def Index():
    return readStudentUseCase.readStudents()


@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):

    if deleteStudentUseCase.deleteStudent(id_data):
        message = "El alumno fue eliminado correctamente"
    else:
        message = "Error: Surgión un error en la eliminación del alumno"

    flash(message)
    return redirect(url_for('Index'))


@app.route('/insert', methods=['POST'])
def insert():
    if addStudentUseCase.addStudent(request):
        message = "El alumno fue ingresado correctamente"
    else:
        message = "Error: El email ya se encuentra registrado. Por favor cambielo"

    flash(message)
    return redirect(url_for('Index'))


@app.route('/update', methods=['POST', 'GET'])
def update():
    if updateStudentUseCase.updateStudent(request):
        message = "El alumno fue actualizado correctamente"
    else:
        message = "Error: El email ya se encuentra registrado. Por favor cambielo"

    flash(message)
    return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)
