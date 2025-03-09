pipeline {
    agent any

    environment {
        // Définir les variables d'environnement nécessaires
        DATABASE_URL = 'postgresql://postgres:passer@localhost:5433/gestion_ecole'
        FLASK_APP = 'run.py'
        FLASK_ENV = 'production'
    }

    stages {
        stage('Checkout') {
            steps {
                // Récupérer le code source depuis le dépôt Git
                git branch: 'main', url: 'https://github.com/morndiaye2007/flask-school-management.git'
                
                
            }
        }

        stage('Install Dependencies') {
            steps {
                // Installer les dépendances Python
                sh 'pip install -r requirements.txt'
                // Installer pytest et pytest-flask pour les tests
                sh 'pip install pytest pytest-flask'
            }
        }

        stage('Run Tests') {
            steps {
                // Exécuter les tests unitaires avec pytest
                sh 'pytest --junitxml=test-results.xml'  // Générer un rapport JUnit pour Jenkins
            }
            post {
                always {
                    // Archiver les résultats des tests
                    junit 'test-results.xml'
                }
            }
        }

        stage('Deploy') {
            steps {
                // Déployer l'application Flask avec Gunicorn
                sh 'gunicorn --bind 0.0.0.0:5000 run:app'
            }
        }
    }

    post {
        always {
            // Nettoyer après la construction
            cleanWs()
        }
        success {
            // Notifier en cas de succès
            echo 'Build and deployment successful!'
        }
        failure {
            // Notifier en cas d'échec
            echo 'Build or deployment failed!'
        }
    }
}