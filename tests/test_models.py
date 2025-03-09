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
        
    def test_teacher_model(self):
        # Test de création d'un professeur
        teacher = Teacher(name='Marie Martin', subject='Mathématiques')
        db.session.add(teacher)
        db.session.commit()
        
        # Vérifier que le professeur a été créé correctement
        saved_teacher = Teacher.query.filter_by(name='Marie Martin').first()
        self.assertIsNotNone(saved_teacher)
        self.assertEqual(saved_teacher.subject, 'Mathématiques')
        
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
        
    def test_schedule_model(self):
        # Créer les objets nécessaires
        course = Course(name='Algèbre linéaire', description='Étude des espaces vectoriels')
        teacher = Teacher(name='Marie Martin', subject='Mathématiques')
        classroom = Classroom(name='Salle 101', capacity=30)
        
        db.session.add_all([course, teacher, classroom])
        db.session.commit()
        
        # Test de création d'un emploi du temps
        schedule = Schedule(
            course_id=course.id,
            teacher_id=teacher.id,
            classroom_id=classroom.id,
            time='Lundi 10h-12h'
        )
        db.session.add(schedule)
        db.session.commit()
        
        # Vérifier que l'emploi du temps a été créé correctement
        saved_schedule = Schedule.query.filter_by(time='Lundi 10h-12h').first()
        self.assertIsNotNone(saved_schedule)
        self.assertEqual(saved_schedule.course_id, course.id)
        self.assertEqual(saved_schedule.teacher_id, teacher.id)
        self.assertEqual(saved_schedule.classroom_id, classroom.id)