from flask import jsonify, request, abort, current_app
from .models import Student, Teacher, Course, Classroom, Schedule
from flask import render_template


def init_routes(app, db):
    @app.route('/')
    def index():
        return render_template('index.html')

    # Routes pour les étudiants
    @app.route('/students', methods=['GET'])
    def get_students():
        students = db.session.query(Student).all()
        return render_template('index.html', students=students)

    @app.route('/students/<int:student_id>', methods=['GET'])
    def get_student(student_id):
        student = db.session.query(Student).get_or_404(student_id)
        return jsonify({'id': student.id, 'name': student.name, 'age': student.age, 'grade': student.grade})

    @app.route('/students', methods=['POST'])
    def add_student():
        if request.content_type == 'application/json':
            data = request.json
        else:
            data = request.form  

        if not data or 'name' not in data or 'age' not in data:
            abort(400, description="Invalid student data")

        student = Student(
        name=data['name'],
        age=data.get('age', ''),
        grade=data.get('grade', '')
        )
        db.session.add(student)
        db.session.commit()

        return jsonify({'id': student.id, 'name': student.name, 'age': student.age}), 201


    @app.route('/students/<int:student_id>', methods=['PUT'])
    def update_student(student_id):
        student = db.session.query(Student).get_or_404(student_id)
        data = request.json
        if not data:
            abort(400, description="No data provided")
        student.name = data.get('name', student.name)
        student.age = data.get('age', student.age)
        student.grade = data.get('grade', student.grade)
        db.session.commit()
        return jsonify({'id': student.id, 'name': student.name, 'age': student.age, 'grade': student.grade})

    @app.route('/students/<int:student_id>', methods=['DELETE'])
    def delete_student(student_id):
        student = db.session.query(Student).get_or_404(student_id)
        db.session.delete(student)
        db.session.commit()
        return jsonify({'result': True})

    # Routes pour les professeurs
    @app.route('/teachers', methods=['GET'])
    def get_teachers():
        teachers = db.session.query(Teacher).all()
        return jsonify([{'id': t.id, 'name': t.name, 'subject': t.subject} for t in teachers])

    @app.route('/teachers/<int:teacher_id>', methods=['GET'])
    def get_teacher(teacher_id):
        teacher = db.session.query(Teacher).get_or_404(teacher_id)
        return jsonify({'id': teacher.id, 'name': teacher.name, 'subject': teacher.subject})

    @app.route('/teachers', methods=['POST'])
    def add_teacher():
        if request.content_type == 'application/json':  # Vérifie si la requête est en JSON
            data = request.json
        else:
            data = request.form  # Récupère les données du formulaire HTML

        if not data or 'name' not in data or 'subject' not in data:
            abort(400, description="Invalid teacher data")

        teacher = Teacher(
            name=data['name'],
            subject=data['subject']
        )
        db.session.add(teacher)
        db.session.commit()
        return jsonify({'id': teacher.id, 'name': teacher.name, 'subject': teacher.subject}), 201

    @app.route('/teachers/<int:teacher_id>', methods=['PUT'])
    def update_teacher(teacher_id):
        teacher = db.session.query(Teacher).get_or_404(teacher_id)
        data = request.json
        if not data:
            abort(400, description="No data provided")
        teacher.name = data.get('name', teacher.name)
        teacher.subject = data.get('subject', teacher.subject)
        db.session.commit()
        return jsonify({'id': teacher.id, 'name': teacher.name, 'subject': teacher.subject})

    @app.route('/teachers/<int:teacher_id>', methods=['DELETE'])
    def delete_teacher(teacher_id):
        teacher = db.session.query(Teacher).get_or_404(teacher_id)
        db.session.delete(teacher)
        db.session.commit()
        return jsonify({'result': True})

    # Routes pour les cours
    @app.route('/courses', methods=['GET'])
    def get_courses():
        courses = db.session.query(Course).all()
        return jsonify([{'id': c.id, 'name': c.name, 'description': c.description} for c in courses])

    @app.route('/courses/<int:course_id>', methods=['GET'])
    def get_course(course_id):
        course = db.session.query(Course).get_or_404(course_id)
        return jsonify({'id': course.id, 'name': course.name, 'description': course.description})

    @app.route('/courses', methods=['POST'])
    def add_course():
        if request.content_type == 'application/json':  # Si la requête est en JSON
            data = request.json
        else:  # Sinon, récupérer les données du formulaire HTML
            data = request.form  

        # Vérification des données envoyées
        if not data or 'name' not in data or 'description' not in data:
            abort(400, description="Invalid course data")

        # Création de l'objet Course
        course = Course(
            name=data['name'],
            description=data['description']
        )
        db.session.add(course)
        db.session.commit()

        return jsonify({'id': course.id, 'name': course.name, 'description': course.description}), 201

    @app.route('/courses/<int:course_id>', methods=['PUT'])
    def update_course(course_id):
        course = db.session.query(Course).get_or_404(course_id)
        data = request.json
        if not data:
            abort(400, description="No data provided")
        course.name = data.get('name', course.name)
        course.description = data.get('description', course.description)
        db.session.commit()
        return jsonify({'id': course.id, 'name': course.name, 'description': course.description})

    @app.route('/courses/<int:course_id>', methods=['DELETE'])
    def delete_course(course_id):
        course = db.session.query(Course).get_or_404(course_id)
        db.session.delete(course)
        db.session.commit()
        return jsonify({'result': True})

    # Routes pour les classes
    @app.route('/classrooms', methods=['GET'])
    def get_classrooms():
        classrooms = db.session.query(Classroom).all()
        return jsonify([{'id': c.id, 'name': c.name, 'capacity': c.capacity} for c in classrooms])

    @app.route('/classrooms/<int:classroom_id>', methods=['GET'])
    def get_classroom(classroom_id):
        classroom = db.session.query(Classroom).get_or_404(classroom_id)
        return jsonify({'id': classroom.id, 'name': classroom.name, 'capacity': classroom.capacity})

    @app.route('/classrooms', methods=['POST'])
    def add_classroom():
        if request.content_type == 'application/json':  # Vérifie si la requête est en JSON
            data = request.json
        else:
            data = request.form  # Sinon, récupérer les données du formulaire HTML

    # Vérification des données envoyées
        if not data or 'name' not in data:
            abort(400, description="Invalid class data")

    # Création de l'objet Classroom
        classroom = Classroom(
            name=data['name'],
            capacity=int(data.get('capacity', 0))  # Convertit en entier, avec 0 par défaut si absent
        )
        db.session.add(classroom)
        db.session.commit()

        return jsonify({'id': classroom.id, 'name': classroom.name, 'capacity': classroom.capacity}), 201

    @app.route('/classrooms/<int:classroom_id>', methods=['PUT'])
    def update_classroom(classroom_id):
        classroom = db.session.query(Classroom).get_or_404(classroom_id)
        data = request.json
        if not data:
            abort(400, description="No data provided")
        classroom.name = data.get('name', classroom.name)
        classroom.capacity = data.get('capacity', classroom.capacity)
        db.session.commit()
        return jsonify({'id': classroom.id, 'name': classroom.name, 'capacity': classroom.capacity})

    @app.route('/classrooms/<int:classroom_id>', methods=['DELETE'])
    def delete_classroom(classroom_id):
        classroom = db.session.query(Classroom).get_or_404(classroom_id)
        db.session.delete(classroom)
        db.session.commit()
        return jsonify({'result': True})

    # Routes pour les emplois du temps
    @app.route('/schedules', methods=['GET'])
    def get_schedules():
        schedules = db.session.query(Schedule).all()
        return jsonify([{'id': s.id, 'course_id': s.course_id, 'teacher_id': s.teacher_id, 'classroom_id': s.classroom_id, 'time': s.time} for s in schedules])

    @app.route('/schedules/<int:schedule_id>', methods=['GET'])
    def get_schedule(schedule_id):
        schedule = db.session.query(Schedule).get_or_404(schedule_id)
        return jsonify({'id': schedule.id, 'course_id': schedule.course_id, 'teacher_id': schedule.teacher_id, 'classroom_id': schedule.classroom_id, 'time': schedule.time})

    @app.route('/schedules', methods=['POST'])
    def add_schedule():
        if request.content_type == 'application/json':
            data = request.json
        else:
            data = request.form  

        if not data or 'day' not in data or 'time' not in data or 'course_id' not in data:
            abort(400, description="Invalid schedule data")

        schedule = Schedule(
        course_id=data['course_id'],
        teacher_id=data.get('teacher_id', ''),
        classroom_id=data.get('classroom_id', ''),
        time=data.get('time', '')
        )
        db.session.add(schedule)
        db.session.commit()

        return jsonify({'id': schedule.id, 'course_id': schedule.course_id, 'teacher_id': schedule.teacher_id, 'classroom_id': schedule.classroom_id, 'time': schedule.time}), 201

    @app.route('/schedules/<int:schedule_id>', methods=['PUT'])
    def update_schedule(schedule_id):
        schedule = db.session.query(Schedule).get_or_404(schedule_id)
        data = request.json
        if not data:
            abort(400, description="No data provided")
        schedule.course_id = data.get('course_id', schedule.course_id)
        schedule.teacher_id = data.get('teacher_id', schedule.teacher_id)
        schedule.classroom_id = data.get('classroom_id', schedule.classroom_id)
        schedule.time = data.get('time', schedule.time)
        db.session.commit()
        return jsonify({'id': schedule.id, 'course_id': schedule.course_id, 'teacher_id': schedule.teacher_id, 'classroom_id': schedule.classroom_id, 'time': schedule.time})

    @app.route('/schedules/<int:schedule_id>', methods=['DELETE'])
    def delete_schedule(schedule_id):
        schedule = db.session.query(Schedule).get_or_404(schedule_id)
        db.session.delete(schedule)
        db.session.commit()
        return jsonify({'result': True})