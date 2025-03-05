from app.models import Student, Teacher, Course, Classroom, Schedule
from app import db

def test_create_student(client):
    student = Student(name="John Doe", age=20, grade="A")
    db.session.add(student)
    db.session.commit()

    assert student.id is not None
    assert student.name == "John Doe"
    assert student.age == 20
    assert student.grade == "A"

def test_create_teacher(client):
    teacher = Teacher(name="Jane Smith", subject="Math")
    db.session.add(teacher)
    db.session.commit()

    assert teacher.id is not None
    assert teacher.name == "Jane Smith"
    assert teacher.subject == "Math"

def test_create_course(client):
    course = Course(name="Physics 101", description="Introduction to Physics")
    db.session.add(course)
    db.session.commit()

    assert course.id is not None
    assert course.name == "Physics 101"
    assert course.description == "Introduction to Physics"

def test_create_classroom(client):
    classroom = Classroom(name="Room A", capacity=30)
    db.session.add(classroom)
    db.session.commit()

    assert classroom.id is not None
    assert classroom.name == "Room A"
    assert classroom.capacity == 30

def test_create_schedule(client):
    course = Course(name="Chemistry 101", description="Basic Chemistry")
    teacher = Teacher(name="Dr. Brown", subject="Chemistry")
    classroom = Classroom(name="Lab 1", capacity=20)

    db.session.add_all([course, teacher, classroom])
    db.session.commit()

    schedule = Schedule(course_id=course.id, teacher_id=teacher.id, classroom_id=classroom.id, time="10:00 AM")
    db.session.add(schedule)
    db.session.commit()

    assert schedule.id is not None
    assert schedule.course_id == course.id
    assert schedule.teacher_id == teacher.id
    assert schedule.classroom_id == classroom.id
    assert schedule.time == "10:00 AM"
