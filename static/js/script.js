document.addEventListener('DOMContentLoaded', function () {
    const studentForm = document.getElementById('studentForm');
    const studentList = document.getElementById('studentList');
    const teacherForm = document.getElementById('teacherForm');
    const teacherList = document.getElementById('teacherList');
    const courseForm = document.getElementById('courseForm');
    const courseList = document.getElementById('courseList');
    const classroomForm = document.getElementById('classroomForm');
    const classroomList = document.getElementById('classroomList');
    const scheduleForm = document.getElementById('scheduleForm');
    const scheduleList = document.getElementById('scheduleList');

    // Charger les données au démarrage
    fetchStudents();
    fetchTeachers();
    fetchCourses();
    fetchClassrooms();
    fetchSchedules();

    // Ajouter un étudiant
    studentForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const name = document.getElementById('studentName').value;
        const age = document.getElementById('studentAge').value;
        const grade = document.getElementById('studentGrade').value;

        fetch('/students', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, age, grade }),
        })
        .then(response => response.json())
        .then(data => {
            alert('Student added successfully!');
            fetchStudents();
            studentForm.reset();
        })
        .catch(error => console.error('Error:', error));
    });

    // Ajouter un professeur
    teacherForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const name = document.getElementById('teacherName').value;
        const subject = document.getElementById('teacherSubject').value;

        fetch('/teachers', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, subject }),
        })
        .then(response => response.json())
        .then(data => {
            alert('Teacher added successfully!');
            fetchTeachers();
            teacherForm.reset();
        })
        .catch(error => console.error('Error:', error));
    });

    // Ajouter un cours
    courseForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const name = document.getElementById('courseName').value;
        const description = document.getElementById('courseDescription').value;

        fetch('/courses', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, description }),
        })
        .then(response => response.json())
        .then(data => {
            alert('Course added successfully!');
            fetchCourses();
            courseForm.reset();
        })
        .catch(error => console.error('Error:', error));
    });

    // Ajouter une classe
    classroomForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const name = document.getElementById('classroomName').value;
        const capacity = document.getElementById('classroomCapacity').value;

        fetch('/classrooms', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, capacity }),
        })
        .then(response => response.json())
        .then(data => {
            alert('Classroom added successfully!');
            fetchClassrooms();
            classroomForm.reset();
        })
        .catch(error => console.error('Error:', error));
    });

    // Ajouter un emploi du temps
    scheduleForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const courseId = document.getElementById('scheduleCourseId').value;
        const teacherId = document.getElementById('scheduleTeacherId').value;
        const classroomId = document.getElementById('scheduleClassroomId').value;
        const time = document.getElementById('scheduleTime').value;

        fetch('/schedules', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ course_id: courseId, teacher_id: teacherId, classroom_id: classroomId, time }),
        })
        .then(response => response.json())
        .then(data => {
            alert('Schedule added successfully!');
            fetchSchedules();
            scheduleForm.reset();
        })
        .catch(error => console.error('Error:', error));
    });

    // Fonction pour afficher le formulaire de modification
    function showEditForm(formId, data) {
        const form = document.getElementById(formId);
        form.style.display = 'block';

        // Remplir le formulaire avec les données existantes
        if (formId === 'editStudentForm') {
            document.getElementById('editStudentId').value = data.id;
            document.getElementById('editStudentName').value = data.name;
            document.getElementById('editStudentAge').value = data.age;
            document.getElementById('editStudentGrade').value = data.grade;
        } else if (formId === 'editTeacherForm') {
            document.getElementById('editTeacherId').value = data.id;
            document.getElementById('editTeacherName').value = data.name;
            document.getElementById('editTeacherSubject').value = data.subject;
        } else if (formId === 'editCourseForm') {
            document.getElementById('editCourseId').value = data.id;
            document.getElementById('editCourseName').value = data.name;
            document.getElementById('editCourseDescription').value = data.description;
        } else if (formId === 'editClassroomForm') {
            document.getElementById('editClassroomId').value = data.id;
            document.getElementById('editClassroomName').value = data.name;
            document.getElementById('editClassroomCapacity').value = data.capacity;
        } else if (formId === 'editScheduleForm') {
            document.getElementById('editScheduleId').value = data.id;
            document.getElementById('editScheduleCourseId').value = data.course_id;
            document.getElementById('editScheduleTeacherId').value = data.teacher_id;
            document.getElementById('editScheduleClassroomId').value = data.classroom_id;
            document.getElementById('editScheduleTime').value = data.time;
        }
    }

    // Fonction pour annuler la modification
    function cancelEdit(formId) {
        document.getElementById(formId).style.display = 'none';
    }

    // Ajouter des boutons "Modifier" aux listes
    function addEditButtons(listId, formId, fetchFunction) {
        const list = document.getElementById(listId);
        list.addEventListener('click', function (e) {
            if (e.target && e.target.classList.contains('edit-btn')) {
                const itemId = e.target.getAttribute('data-id');
                fetch(`/${listId.replace('List', 's')}/${itemId}`)
                    .then(response => response.json())
                    .then(data => showEditForm(formId, data))
                    .catch(error => console.error('Error:', error));
            }
        });
    }

    // Ajouter des boutons "Modifier" pour chaque entité
    addEditButtons('studentList', 'editStudentForm', fetchStudents);
    addEditButtons('teacherList', 'editTeacherForm', fetchTeachers);
    addEditButtons('courseList', 'editCourseForm', fetchCourses);
    addEditButtons('classroomList', 'editClassroomForm', fetchClassrooms);
    addEditButtons('scheduleList', 'editScheduleForm', fetchSchedules);

    // Soumission du formulaire de modification pour les étudiants
    document.getElementById('updateStudentForm').addEventListener('submit', function (e) {
        e.preventDefault();
        const id = document.getElementById('editStudentId').value;
        const name = document.getElementById('editStudentName').value;
        const age = document.getElementById('editStudentAge').value;
        const grade = document.getElementById('editStudentGrade').value;

        fetch(`/students/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, age, grade }),
        })
        .then(response => response.json())
        .then(data => {
            alert('Student updated successfully!');
            fetchStudents();
            cancelEdit('editStudentForm');
        })
        .catch(error => console.error('Error:', error));
    });

    // Soumission du formulaire de modification pour les professeurs
    document.getElementById('updateTeacherForm').addEventListener('submit', function (e) {
        e.preventDefault();
        const id = document.getElementById('editTeacherId').value;
        const name = document.getElementById('editTeacherName').value;
        const subject = document.getElementById('editTeacherSubject').value;

        fetch(`/teachers/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, subject }),
        })
        .then(response => response.json())
        .then(data => {
            alert('Teacher updated successfully!');
            fetchTeachers();
            cancelEdit('editTeacherForm');
        })
        .catch(error => console.error('Error:', error));
    });

    // Soumission du formulaire de modification pour les cours
    document.getElementById('updateCourseForm').addEventListener('submit', function (e) {
        e.preventDefault();
        const id = document.getElementById('editCourseId').value;
        const name = document.getElementById('editCourseName').value;
        const description = document.getElementById('editCourseDescription').value;

        fetch(`/courses/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, description }),
        })
        .then(response => response.json())
        .then(data => {
            alert('Course updated successfully!');
            fetchCourses();
            cancelEdit('editCourseForm');
        })
        .catch(error => console.error('Error:', error));
    });

    // Soumission du formulaire de modification pour les classes
    document.getElementById('updateClassroomForm').addEventListener('submit', function (e) {
        e.preventDefault();
        const id = document.getElementById('editClassroomId').value;
        const name = document.getElementById('editClassroomName').value;
        const capacity = document.getElementById('editClassroomCapacity').value;

        fetch(`/classrooms/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, capacity }),
        })
        .then(response => response.json())
        .then(data => {
            alert('Classroom updated successfully!');
            fetchClassrooms();
            cancelEdit('editClassroomForm');
        })
        .catch(error => console.error('Error:', error));
    });

    // Soumission du formulaire de modification pour les emplois du temps
    document.getElementById('updateScheduleForm').addEventListener('submit', function (e) {
        e.preventDefault();
        const id = document.getElementById('editScheduleId').value;
        const courseId = document.getElementById('editScheduleCourseId').value;
        const teacherId = document.getElementById('editScheduleTeacherId').value;
        const classroomId = document.getElementById('editScheduleClassroomId').value;
        const time = document.getElementById('editScheduleTime').value;

        fetch(`/schedules/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ course_id: courseId, teacher_id: teacherId, classroom_id: classroomId, time }),
        })
        .then(response => response.json())
        .then(data => {
            alert('Schedule updated successfully!');
            fetchSchedules();
            cancelEdit('editScheduleForm');
        })
        .catch(error => console.error('Error:', error));
    });

    // Fonctions pour récupérer les données
    function fetchStudents() {
        fetch('/students')
            .then(response => response.json())
            .then(data => {
                studentList.innerHTML = '';
                data.forEach(student => {
                    const li = document.createElement('li');
                    li.textContent = `${student.name} - ${student.age} years old - Grade: ${student.grade}`;
                    const editButton = document.createElement('button');
                    editButton.textContent = 'Edit';
                    editButton.classList.add('edit-btn');
                    editButton.setAttribute('data-id', student.id);
                    li.appendChild(editButton);
                    studentList.appendChild(li);
                });
            })
            .catch(error => console.error('Error:', error));
    }

    function fetchTeachers() {
        fetch('/teachers')
            .then(response => response.json())
            .then(data => {
                teacherList.innerHTML = '';
                data.forEach(teacher => {
                    const li = document.createElement('li');
                    li.textContent = `${teacher.name} - Subject: ${teacher.subject}`;
                    const editButton = document.createElement('button');
                    editButton.textContent = 'Edit';
                    editButton.classList.add('edit-btn');
                    editButton.setAttribute('data-id', teacher.id);
                    li.appendChild(editButton);
                    teacherList.appendChild(li);
                });
            })
            .catch(error => console.error('Error:', error));
    }

    function fetchCourses() {
        fetch('/courses')
            .then(response => response.json())
            .then(data => {
                courseList.innerHTML = '';
                data.forEach(course => {
                    const li = document.createElement('li');
                    li.textContent = `${course.name} - Description: ${course.description}`;
                    const editButton = document.createElement('button');
                    editButton.textContent = 'Edit';
                    editButton.classList.add('edit-btn');
                    editButton.setAttribute('data-id', course.id);
                    li.appendChild(editButton);
                    courseList.appendChild(li);
                });
            })
            .catch(error => console.error('Error:', error));
    }

    function fetchClassrooms() {
        fetch('/classrooms')
            .then(response => response.json())
            .then(data => {
                classroomList.innerHTML = '';
                data.forEach(classroom => {
                    const li = document.createElement('li');
                    li.textContent = `${classroom.name} - Capacity: ${classroom.capacity}`;
                    const editButton = document.createElement('button');
                    editButton.textContent = 'Edit';
                    editButton.classList.add('edit-btn');
                    editButton.setAttribute('data-id', classroom.id);
                    li.appendChild(editButton);
                    classroomList.appendChild(li);
                });
            })
            .catch(error => console.error('Error:', error));
    }

    function fetchSchedules() {
        fetch('/schedules')
            .then(response => response.json())
            .then(data => {
                scheduleList.innerHTML = '';
                data.forEach(schedule => {
                    const li = document.createElement('li');
                    li.textContent = `Course ID: ${schedule.course_id}, Teacher ID: ${schedule.teacher_id}, Classroom ID: ${schedule.classroom_id}, Time: ${schedule.time}`;
                    const editButton = document.createElement('button');
                    editButton.textContent = 'Edit';
                    editButton.classList.add('edit-btn');
                    editButton.setAttribute('data-id', schedule.id);
                    li.appendChild(editButton);
                    scheduleList.appendChild(li);
                });
            })
            .catch(error => console.error('Error:', error));
    }
});