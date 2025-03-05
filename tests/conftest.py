import pytest
from app import app, db
from app.models import Student, Teacher, Course, Classroom, Schedule

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:passer@localhost:5432/gestion_ecole'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()
