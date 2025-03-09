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
        
        # Créer un client de test
        self.client = self.app.test_client()
        
        # Ajouter quelques données de test
        student1 = Student(name='Jean Dupont', age=18, grade='Terminale')
        student2 = Student(name='Alice Martin', age=17, grade='Première')
        db.session.add_all([student1, student2])
        db.session.commit()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
    def test_get_students(self):
        # Tester la récupération de tous les étudiants
        response = self.client.get('/students')
        self.assertEqual(response.status_code, 200)
        
    def test_get_student(self):
        # Tester la récupération d'un étudiant spécifique
        student = Student.query.filter_by(name='Jean Dupont').first()
        response = self.client.get(f'/students/{student.id}')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'Jean Dupont')
        self.assertEqual(data['age'], 18)
        self.assertEqual(data['grade'], 'Terminale')
        
    def test_add_student_json(self):
        # Tester l'ajout d'un étudiant via JSON
        new_student = {
            'name': 'Paul Bernard',
            'age': 16,
            'grade': 'Seconde'
        }
        
        response = self.client.post(
            '/students',
            data=json.dumps(new_student),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 201)
        
        # Vérifier que l'étudiant a été ajouté en base
        added_student = Student.query.filter_by(name='Paul Bernard').first()
        self.assertIsNotNone(added_student)
        self.assertEqual(added_student.age, 16)
        self.assertEqual(added_student.grade, 'Seconde')
        
    def test_add_student_form(self):
        # Tester l'ajout d'un étudiant via formulaire
        new_student = {
            'name': 'Sophie Dubois',
            'age': 15,
            'grade': 'Troisième'
        }
        
        response = self.client.post(
            '/students',
            data=new_student
        )
        
        # Redirection après création
        self.assertEqual(response.status_code, 302)
        
        # Vérifier que l'étudiant a été ajouté en base
        added_student = Student.query.filter_by(name='Sophie Dubois').first()
        self.assertIsNotNone(added_student)
        self.assertEqual(added_student.age, 15)
        self.assertEqual(added_student.grade, 'Troisième')
        
    def test_update_student(self):
        # Tester la mise à jour d'un étudiant
        student = Student.query.filter_by(name='Jean Dupont').first()
        
        updated_data = {
            'name': 'Jean Dupont',
            'age': 19,
            'grade': 'Licence'
        }
        
        response = self.client.put(
            f'/students/{student.id}',
            data=json.dumps(updated_data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        
        # Vérifier que l'étudiant a été mis à jour
        updated_student = Student.query.get(student.id)
        self.assertEqual(updated_student.age, 19)
        self.assertEqual(updated_student.grade, 'Licence')
        
    def test_delete_student(self):
        # Tester la suppression d'un étudiant
        student = Student.query.filter_by(name='Alice Martin').first()
        
        response = self.client.delete(f'/students/{student.id}')
        
        self.assertEqual(response.status_code, 200)
        
        # Vérifier que l'étudiant a été supprimé
        deleted_student = Student.query.get(student.id)
        self.assertIsNone(deleted_student)
        
    def test_get_nonexistent_student(self):
        # Tester la récupération d'un étudiant qui n'existe pas
        response = self.client.get('/students/999')
        self.assertEqual(response.status_code, 404)