import pytest
from app.models import Student, Teacher, db
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

def test_student_model(app):
    with app.app_context():
        student = Student(name="John Doe", age=20, grade="A")
        db.session.add(student)
        db.session.commit()
        assert student.id is not None
        assert student.name == "John Doe"
        assert student.age == 20
        assert student.grade == "A"