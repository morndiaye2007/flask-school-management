from app.models import Student, Teacher, Course, Classroom, Schedule

def test_student_model(app):
    with app.app_context():
        student = Student(name='Moussa Diop', age=20, grade='A')
        assert student.name == 'Moussa Diop'
        assert student.age == 20
        assert student.grade == 'A'

def test_teacher_model(app):
    with app.app_context():
        teacher = Teacher(name='Mr. Ndiaye', subject='Math')
        assert teacher.name == 'Mr. Ndiaye'
        assert teacher.subject == 'Math'