from flask import Blueprint, render_template, request, redirect, url_for
from models.medico import Medico
from config import db

medico_bp = Blueprint('medico', __name__)

@medico_bp.route('/medicos')
def listar_medicos():
    medicos = Medico.query.all()
    return render_template('medicos.html', medicos=medicos)

@medico_bp.route('/medico/nuevo', methods=['POST'])
def nuevo_medico():
    nombre = request.form['nombre']
    especialidad = request.form['especialidad']
    telefono = request.form['telefono']
    correo = request.form['correo']
    medico = Medico(nombre=nombre, especialidad=especialidad, telefono=telefono, correo=correo)
    db.session.add(medico)
    db.session.commit()
    return redirect(url_for('medico.listar_medicos'))
# Editar médico
@medico_bp.route('/medico/editar/<int:id>', methods=['GET', 'POST'])
def editar_medico(id):
    medico = Medico.query.get_or_404(id)
    if request.method == 'POST':
        medico.nombre = request.form['nombre']
        medico.especialidad = request.form['especialidad']
        medico.telefono = request.form['telefono']
        medico.correo = request.form['correo']
        db.session.commit()
        return redirect(url_for('medico.listar_medicos'))
    return render_template('editar_medico.html', medico=medico)

# Eliminar médico
@medico_bp.route('/medico/eliminar/<int:id>', methods=['POST'])
def eliminar_medico(id):
    medico = Medico.query.get_or_404(id)
    db.session.delete(medico)
    db.session.commit()
    return redirect(url_for('medico.listar_medicos'))