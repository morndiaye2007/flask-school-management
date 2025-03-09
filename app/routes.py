from flask import jsonify, request, abort, current_app, render_template, redirect, url_for
from .models import Student, Teacher, Course, Classroom, Schedule
from sqlalchemy import desc

def init_routes(app, db):
    @app.route('/')
    def index():
        return render_template('layout.html')

    # Routes pour les étudiants
    @app.route('/students', methods=['GET'])
    def get_students():
        students = db.session.query(Student).all()
        return render_template('students.html', students=students)

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

        if not data or 'name' not in data:
            abort(400, description="Invalid student data")

        # Conversion explicite des types
        name = data.get('name', '')
        age = data.get('age', '')
        grade = data.get('grade', '')

        student = Student(
            name=name,
            age=age,
            grade=grade
        )
        db.session.add(student)
        db.session.commit()

        # Si la requête vient d'un appel AJAX, renvoyer JSON
        if request.is_json:
            return jsonify({'id': student.id, 'name': student.name, 'age': student.age, 'grade': student.grade}), 201
        else:
            # Sinon rediriger vers la liste des étudiants
            return redirect(url_for('get_students'))

    @app.route('/students/<int:student_id>', methods=['PUT'])
    def update_student(student_id):
        student = db.session.query(Student).get_or_404(student_id)
        
        if request.content_type == 'application/json':
            data = request.json
        else:
            data = request.form
            
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
        return render_template('teachers.html', teachers=teachers)

    @app.route('/teachers/<int:teacher_id>', methods=['GET'])
    def get_teacher(teacher_id):
        teacher = db.session.query(Teacher).get_or_404(teacher_id)
        return jsonify({'id': teacher.id, 'name': teacher.name, 'subject': teacher.subject})

    @app.route('/teachers', methods=['POST'])
    def add_teacher():
        if request.content_type == 'application/json':
            data = request.json
        else:
            data = request.form

        if not data or 'name' not in data or 'subject' not in data:
            abort(400, description="Invalid teacher data")

        teacher = Teacher(
            name=data['name'],
            subject=data['subject']
        )
        db.session.add(teacher)
        db.session.commit()
        
        if request.is_json:
            return jsonify({'id': teacher.id, 'name': teacher.name, 'subject': teacher.subject}), 201
        else:
            return redirect(url_for('get_teachers'))

    @app.route('/teachers/<int:teacher_id>', methods=['PUT'])
    def update_teacher(teacher_id):
        teacher = db.session.query(Teacher).get_or_404(teacher_id)
        
        if request.content_type == 'application/json':
            data = request.json
        else:
            data = request.form
            
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
        return render_template('courses.html', courses=courses)

    @app.route('/courses/<int:course_id>', methods=['GET'])
    def get_course(course_id):
        course = db.session.query(Course).get_or_404(course_id)
        return jsonify({'id': course.id, 'name': course.name, 'description': course.description})

    @app.route('/courses', methods=['POST'])
    def add_course():
        if request.content_type == 'application/json':
            data = request.json
        else:
            data = request.form

        if not data or 'name' not in data or 'description' not in data:
            abort(400, description="Invalid course data")

        course = Course(
            name=data['name'],
            description=data['description']
        )
        db.session.add(course)
        db.session.commit()

        if request.is_json:
            return jsonify({'id': course.id, 'name': course.name, 'description': course.description}), 201
        else:
            return redirect(url_for('get_courses'))

    @app.route('/courses/<int:course_id>', methods=['PUT'])
    def update_course(course_id):
        course = db.session.query(Course).get_or_404(course_id)
        
        if request.content_type == 'application/json':
            data = request.json
        else:
            data = request.form
            
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
        return render_template('classrooms.html', classrooms=classrooms)

    @app.route('/classrooms/<int:classroom_id>', methods=['GET'])
    def get_classroom(classroom_id):
        classroom = db.session.query(Classroom).get_or_404(classroom_id)
        return jsonify({'id': classroom.id, 'name': classroom.name, 'capacity': classroom.capacity})

    @app.route('/classrooms', methods=['POST'])
    def add_classroom():
        if request.content_type == 'application/json':
            data = request.json
        else:
            data = request.form

        if not data or 'name' not in data:
            abort(400, description="Invalid classroom data")

        # Conversion explicite de la capacité en entier
        try:
            capacity = int(data.get('capacity', 0))
        except ValueError:
            capacity = 0

        classroom = Classroom(
            name=data['name'],
            capacity=capacity
        )
        db.session.add(classroom)
        db.session.commit()

        if request.is_json:
            return jsonify({'id': classroom.id, 'name': classroom.name, 'capacity': classroom.capacity}), 201
        else:
            return redirect(url_for('get_classrooms'))

    @app.route('/classrooms/<int:classroom_id>', methods=['PUT'])
    def update_classroom(classroom_id):
        classroom = db.session.query(Classroom).get_or_404(classroom_id)
        
        if request.content_type == 'application/json':
            data = request.json
        else:
            data = request.form
            
        if not data:
            abort(400, description="No data provided")
            
        classroom.name = data.get('name', classroom.name)
        
        # Vérifier et convertir la capacité
        if 'capacity' in data:
            try:
                classroom.capacity = int(data['capacity'])
            except ValueError:
                pass
                
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
        
        # Récupération des données nécessaires pour le template
        courses = db.session.query(Course).all()
        teachers = db.session.query(Teacher).all()
        classrooms = db.session.query(Classroom).all()
        
        # Créer des dictionnaires pour faciliter l'accès aux noms
        course_names = {course.id: course.name for course in courses}
        teacher_names = {teacher.id: teacher.name for teacher in teachers}
        classroom_names = {classroom.id: classroom.name for classroom in classrooms}
        
        return render_template('schedules.html', 
                              schedules=schedules,
                              courses=courses,
                              teachers=teachers,
                              classrooms=classrooms,
                              course_names=course_names,
                              teacher_names=teacher_names,
                              classroom_names=classroom_names)

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

        if not data or 'course_id' not in data or 'teacher_id' not in data or 'classroom_id' not in data or 'time' not in data:
            abort(400, description="Invalid schedule data")

        # Conversion explicite des ID en entiers
        try:
            course_id = int(data['course_id'])
            teacher_id = int(data['teacher_id'])
            classroom_id = int(data['classroom_id'])
        except ValueError:
            abort(400, description="Invalid ID format")

        schedule = Schedule(
            course_id=course_id,
            teacher_id=teacher_id,
            classroom_id=classroom_id,
            time=data['time']
        )
        db.session.add(schedule)
        db.session.commit()

        if request.is_json:
            return jsonify({'id': schedule.id, 'course_id': schedule.course_id, 'teacher_id': schedule.teacher_id, 'classroom_id': schedule.classroom_id, 'time': schedule.time}), 201
        else:
            return redirect(url_for('get_schedules'))
            
    @app.route('/schedules/<int:schedule_id>', methods=['PUT'])
    def update_schedule(schedule_id):
        schedule = db.session.query(Schedule).get_or_404(schedule_id)
        
        if request.content_type == 'application/json':
            data = request.json
        else:
            data = request.form
            
        if not data:
            abort(400, description="No data provided")
            
        # Conversion et validation des données
        if 'course_id' in data:
            try:
                schedule.course_id = int(data['course_id'])
            except ValueError:
                pass
        
        if 'teacher_id' in data:
            try:
                schedule.teacher_id = int(data['teacher_id'])
            except ValueError:
                pass
                
        if 'classroom_id' in data:
            try:
                schedule.classroom_id = int(data['classroom_id'])
            except ValueError:
                pass
                
        schedule.time = data.get('time', schedule.time)
        
        db.session.commit()
        
        return jsonify({'id': schedule.id, 'course_id': schedule.course_id, 'teacher_id': schedule.teacher_id, 'classroom_id': schedule.classroom_id, 'time': schedule.time})

    @app.route('/schedules/<int:schedule_id>', methods=['DELETE'])
    def delete_schedule(schedule_id):
        schedule = db.session.query(Schedule).get_or_404(schedule_id)
        db.session.delete(schedule)
        db.session.commit()
        return jsonify({'result': True})