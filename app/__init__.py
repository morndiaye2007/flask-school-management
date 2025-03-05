from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialisation de SQLAlchemy
db = SQLAlchemy()

# Initialisation de Flask-Migrate
migrate = Migrate()

def create_app():
    # Créer l'application Flask
    app = Flask(__name__)


# Importer les modèles ici
    from app.models import Student

# Rendre db et Student accessibles depuis `app`
    __all__ = ["db", "Student"]

    # Configuration de la base de données PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:passer@localhost:5433/gestion_ecole'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Désactive le suivi des modifications

    # Initialisation de SQLAlchemy avec l'application Flask
    db.init_app(app)

    # Initialisation de Flask-Migrate avec l'application Flask et SQLAlchemy
    migrate.init_app(app, db)

    # Importer et enregistrer les routes en passant explicitement `db`
    from app.routes import init_routes  # Assurez-vous que ce chemin est correct
    init_routes(app, db)  # Passez `db` aux routes

    # Création des tables de la base de données dans le contexte de l'application
    with app.app_context():
        db.create_all()  # Crée les tables si elles n'existent pas déjà

    # Afficher les routes disponibles (pour le débogage)
    print("Routes disponibles :", app.url_map)

    return app