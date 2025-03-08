import pytest
from app import create_app
from app.models import db, Student

@pytest.fixture
def client():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_get_students(client):
    response = client.get('/students')
    assert response.status_code == 200

def test_add_student(client):
    response = client.post('/students', json={
        'name': 'John Doe',
        'age': 20,
        'grade': 'A'
    })
    assert response.status_code == 201
    assert response.json['name'] == 'John Doe'