from flask import Blueprint, render_template, request, redirect, url_for
from models.paciente import Paciente
from config import db

paciente_bp = Blueprint('paciente', __name__)

# 📌 Listar pacientes
@paciente_bp.route('/pacientes')
def listar_pacientes():
    pacientes = Paciente.query.all()
    return render_template('pacientes.html', pacientes=pacientes)

# 📌 Crear nuevo paciente
@paciente_bp.route('/paciente/nuevo', methods=['POST'])
def nuevo_paciente():
    nombre = request.form['nombre']
    edad = request.form['edad']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    paciente = Paciente(nombre=nombre, edad=edad, direccion=direccion, telefono=telefono)
    db.session.add(paciente)
    db.session.commit()
    return redirect(url_for('paciente.listar_pacientes'))

# 📌 Editar paciente
@paciente_bp.route('/paciente/editar/<int:id>', methods=['GET', 'POST'])
def editar_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    if request.method == 'POST':
        paciente.nombre = request.form['nombre']
        paciente.edad = request.form['edad']
        paciente.direccion = request.form['direccion']
        paciente.telefono = request.form['telefono']
        db.session.commit()
        return redirect(url_for('paciente.listar_pacientes'))
    return render_template('editar_paciente.html', paciente=paciente)

# 📌 Eliminar paciente
@paciente_bp.route('/paciente/eliminar/<int:id>')
def eliminar_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    db.session.delete(paciente)
    db.session.commit()
    return redirect(url_for('paciente.listar_pacientes'))
