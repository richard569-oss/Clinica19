from flask import Blueprint, render_template, request, redirect, url_for, session
from models.usuario import Usuario
from config import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        usuario = Usuario.query.filter_by(username=request.form['username']).first()
        if usuario and usuario.check_password(request.form['password']):
            session['usuario'] = usuario.username
            return redirect(url_for('inicio'))
    return render_template('login.html')

@auth_bp.route('/registro', methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        usuario = Usuario(username=request.form['username'])
        usuario.set_password(request.form['password'])
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('registro.html')
