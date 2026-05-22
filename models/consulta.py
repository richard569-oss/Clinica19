from config import db

class Consulta(db.Model):
    id_consulta = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    diagnostico = db.Column(db.String(200))
    tratamiento = db.Column(db.String(200))
    id_medico = db.Column(db.Integer, db.ForeignKey('medico.id_medico'), nullable=False)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'), nullable=False)
