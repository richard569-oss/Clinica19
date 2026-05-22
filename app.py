from flask import render_template
from config import app, db
from controllers.medico_controller import medico_bp
from controllers.paciente_controller import paciente_bp
from controllers.consulta_controller import consulta_bp
from controllers.auth_controller import auth_bp

@app.route("/")
def inicio():
    return render_template("dashboard.html")   # ahora carga el template

# Registrar Blueprints
app.register_blueprint(medico_bp)
app.register_blueprint(paciente_bp)
app.register_blueprint(consulta_bp)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    # ✅ Render necesita host=0.0.0.0 y PORT dinámico
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
