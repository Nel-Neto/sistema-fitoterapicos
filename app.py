from flask import Flask, render_template
from config import Config
from models import db
from routes.plantas import plantas_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(plantas_bp)

    @app.errorhandler(404)
    def pagina_nao_encontrada(error):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def erro_interno(error):
        return render_template("500.html"), 500

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
