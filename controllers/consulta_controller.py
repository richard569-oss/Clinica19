from flask import Blueprint, render_template, request, redirect, url_for
from models.consulta import Consulta
from models.medico import Medico
from models.paciente import Paciente
from config import db
from datetime import datetime


consulta_bp = Blueprint('consulta', __name__)

# 📌 Listar consultas
@consulta_bp.route('/consultas')
def listar_consultas():
    consultas = Consulta.query.all()
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    return render_template('consultas.html', consultas=consultas, medicos=medicos, pacientes=pacientes)

# 📌 Crear nueva consulta
@consulta_bp.route('/consulta/nueva', methods=['POST'])
def nueva_consulta():
    fecha = datetime.strptime(request.form['fecha'], "%Y-%m-%d").date()
    diagnostico = request.form['diagnostico']
    tratamiento = request.form['tratamiento']
    id_medico = request.form['id_medico']
    id_paciente = request.form['id_paciente']

    consulta = Consulta(
        fecha=fecha,
        diagnostico=diagnostico,
        tratamiento=tratamiento,
        id_medico=id_medico,
        id_paciente=id_paciente
    )
    db.session.add(consulta)
    db.session.commit()
    return redirect(url_for('consulta.listar_consultas'))

# 📌 Editar consulta
@consulta_bp.route('/consulta/editar/<int:id>', methods=['GET', 'POST'])
def editar_consulta(id):
    consulta = Consulta.query.get_or_404(id)
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    if request.method == 'POST':
        consulta.fecha = request.form['fecha']
        consulta.diagnostico = request.form['diagnostico']
        consulta.tratamiento = request.form['tratamiento']
        consulta.id_medico = request.form['id_medico']
        consulta.id_paciente = request.form['id_paciente']
        db.session.commit()
        return redirect(url_for('consulta.listar_consultas'))
    return render_template('editar_consulta.html', consulta=consulta, medicos=medicos, pacientes=pacientes)

# 📌 Eliminar consulta
@consulta_bp.route('/consulta/eliminar/<int:id>')
def eliminar_consulta(id):
    consulta = Consulta.query.get_or_404(id)
    db.session.delete(consulta)
    db.session.commit()
    return redirect(url_for('consulta.listar_consultas'))
