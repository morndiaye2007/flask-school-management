pipeline {
    agent {
        docker {
            image 'python:3.9-slim'  // Utilise une image Docker avec Python préinstallé
            args '-v /tmp:/tmp'
        }
    }

    environment {
        DATABASE_URL = 'postgresql://postgres:passer@localhost:5433/gestion_ecole'
        FLASK_APP = 'run.py'
        FLASK_ENV = 'production'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/morndiaye2007/flask-school-management.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pip install pytest pytest-flask'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --junitxml=test-results.xml'
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'gunicorn --bind 0.0.0.0:5000 run:app'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo 'Build and deployment successful!'
        }
        failure {
            echo 'Build or deployment failed!'
        }
    }
}