import unittest
import json
from app import create_app, db
from app.models import Student

class TestStudentRoutes(unittest.TestCase):
    def setUp(self):
        # Créer une application de test avec une base de données en mémoire
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
