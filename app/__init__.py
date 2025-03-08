from flask import Flask
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


# Initialisation de SQLAlchemy
db = SQLAlchemy()

# Initialisation de Flask-Migrate
migrate = Migrate()

def create_app():
    # Créer l'application Flask
    app = Flask(__name__)

    # Configuration de la base de données PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:passer@localhost:5433/gestion_ecole')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Désactive le suivi des modifications

    # Initialisation de SQLAlchemy avec l'application Flask
    db.init_app(app)

    # Initialisation de Flask-Migrate avec l'application Flask et SQLAlchemy
    migrate.init_app(app, db)

    # Importer les modèles ici (après l'initialisation de `db`)
    with app.app_context():
        # Importer les modèles dans le contexte de l'application
        from .models import Student, Teacher, Course, Classroom, Schedule

        # Créer les tables si elles n'existent pas déjà
        db.create_all()

    # Importer et enregistrer les routes
    from app.routes import init_routes
    init_routes(app, db)

    # Tester la connexion à la base de données
    with app.app_context():
        try:
            db.session.execute(text("SELECT 1"))
            print("Connexion à la base de données réussie !")
        except Exception as e:
            print("Erreur de connexion à la base de données :", e)

    # Afficher les routes disponibles (pour le débogage)
    print("Routes disponibles :", app.url_map)

    return app