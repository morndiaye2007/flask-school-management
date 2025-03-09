import unittest
from app import create_app, db
from app.models import Student, Teacher, Course, Classroom, Schedule

class TestModels(unittest.TestCase):
    def setUp(self):
        # Créer une application de test avec une base de données en mémoire
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
    def test_student_model(self):
        # Test de création d'un étudiant
        student = Student(name='Jean Dupont', age=18, grade='Terminale')
        db.session.add(student)
        db.session.commit()
        
        # Vérifier que l'étudiant a été créé correctement
        saved_student = Student.query.filter_by(name='Jean Dupont').first()
        self.assertIsNotNone(saved_student)
        self.assertEqual(saved_student.age, 18)
        self.assertEqual(saved_student.grade, 'Terminale')
        
    def test_course_model(self):
        # Test de création d'un cours
        course = Course(name='Algèbre linéaire', description='Étude des espaces vectoriels')
        db.session.add(course)
        db.session.commit()
        
        # Vérifier que le cours a été créé correctement
        saved_course = Course.query.filter_by(name='Algèbre linéaire').first()
        self.assertIsNotNone(saved_course)
        self.assertEqual(saved_course.description, 'Étude des espaces vectoriels')
        
    def test_classroom_model(self):
        # Test de création d'une salle de classe
        classroom = Classroom(name='Salle 101', capacity=30)
        db.session.add(classroom)
        db.session.commit()
        
        # Vérifier que la salle a été créée correctement
        saved_classroom = Classroom.query.filter_by(name='Salle 101').first()
        self.assertIsNotNone(saved_classroom)
        self.assertEqual(saved_classroom.capacity, 30)
        
       