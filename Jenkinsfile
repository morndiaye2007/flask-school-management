pipeline {
    agent any

    environment {
        // Variables d'environnement
        DATABASE_URL = 'postgresql://postgres:passer@localhost:5433/gestion_ecole'
        FLASK_APP = 'run.py'
        FLASK_ENV = 'production'
        SONAR_PROJECT_KEY = 'my-flask-app' // Clé du projet SonarQube
        SONAR_PROJECT_NAME = 'My Flask App' // Nom du projet SonarQube
        SONAR_HOST_URL = 'http://localhost:9000' // URL de SonarQube
        SONAR_TOKEN = credentials('sonar-token') // Token SonarQube
        PYTHON_PATH = 'C:\\laragon\\bin\\python\\python-3.10\\Scripts\\' // Chemin vers Python et pip
    }

    stages {
        // Étape 1 : Récupération du code source depuis GitHub
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/morndiaye2007/flask-school-management.git'
            }
        }

        // Étape 2 : Installation des dépendances
        stage('Install Dependencies') {
            steps {
                bat "${PYTHON_PATH}pip install -r requirements.txt"
                bat "${PYTHON_PATH}pip install pytest pytest-cov pytest-flask selenium" // Ajoutez selenium pour les tests IHM
            }
        }

        // Étape 3 : Exécution des tests unitaires
        stage('Run Unit Tests') {
            steps {
                bat "${PYTHON_PATH}pytest tests/unit/ --junitxml=unit-test-results.xml --cov=app --cov-report=xml"
            }
            post {
                always {
                    // Publier les résultats des tests unitaires
                    junit 'unit-test-results.xml'
                }
            }
        }

        // Étape 4 : Exécution des tests IHM
        stage('Run IHM Tests') {
            steps {
                bat "${PYTHON_PATH}pytest tests/ihm/ --junitxml=ihm-test-results.xml"
            }
            post {
                always {
                    // Publier les résultats des tests IHM
                    junit 'ihm-test-results.xml'
                }
            }
        }

        // Étape 5 : Analyse de la qualité du code avec SonarQube
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') { // Nom de la configuration SonarQube dans Jenkins
                    bat """
                        ${PYTHON_PATH}sonar-scanner.bat \
                        -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                        -Dsonar.projectName=${SONAR_PROJECT_NAME} \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=${SONAR_HOST_URL} \
                        -Dsonar.login=${SONAR_TOKEN} \
                        -Dsonar.python.version=3.10 \
                        -Dsonar.python.coverage.reportPaths=coverage.xml
                    """
                }
            }
        }

        // Étape 6 : Déploiement de l'application Flask
        stage('Deploy') {
            steps {
                bat """
                    set FLASK_APP=${FLASK_APP}
                    set FLASK_ENV=${FLASK_ENV}
                    set DATABASE_URL=${DATABASE_URL}

                    REM Arrêter le service existant si nécessaire
                    taskkill /F /IM python.exe /FI "WINDOWTITLE eq Flask*" 2>NUL

                    REM Démarrer l'application en arrière-plan
                    start /B ${PYTHON_PATH}python.exe -m flask run --host=0.0.0.0 --port=5000

                    echo Application déployée avec succès
                """
            }
        }
    }

    post {
        always {
            node {
                cleanWs(deleteDirs: true, notFailBuild: true)
            }
        }
        success {
            echo 'Le déploiement a réussi !'
        }
        failure {
            echo 'La construction ou le déploiement a échoué !'
        }
    }
}