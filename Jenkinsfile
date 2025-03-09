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
                git branch: 'master', url: 'https://github.com/morndiaye2007/flask-school-management.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Utiliser bat au lieu de sh pour Windows
                bat 'pip install -r requirements.txt'
                // Installer pytest pour les tests
                bat 'pip install pytest pytest-flask'
            }
        }

        stage('Run Tests') {
            steps {
                // Exécuter les tests avec pytest
                bat 'pytest'
            }
        }

        stage('Deploy') {
            steps {
                // Déployer l'application Flask
                // Vous pouvez utiliser un script batch pour démarrer votre application
                bat '''
                    echo Déploiement de l\'application Flask
                    set FLASK_APP=%FLASK_APP%
                    set FLASK_ENV=%FLASK_ENV%
                    set DATABASE_URL=%DATABASE_URL%
                    
                    REM Arrêter le service existant si nécessaire (à adapter selon votre configuration)
                    REM taskkill /F /IM python.exe /FI "WINDOWTITLE eq Flask*" 2>NUL
                    
                    REM Démarrer l'application en arrière-plan
                    start /B python -m flask run --host=0.0.0.0 --port=5000
                    
                    echo Application déployée avec succès
                '''
            }
        }
    }

    post {
        success {
            echo 'Le déploiement a réussi !'
        }
        failure {
            echo 'La construction ou le déploiement a échoué !'
            // Nettoyage en cas d'échec
            cleanWs()
        }
    }
}


