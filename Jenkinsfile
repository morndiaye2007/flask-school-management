pipeline {
    agent {
        docker {
            image 'python:3.9-slim'  // Utilisation d'une image Python 3.9
            args '-v /tmp:/tmp'      // Montage du volume /tmp pour le partage de fichiers
            reuseNode true          // Réutiliser le nœud pour éviter de recréer un conteneur à chaque étape
        }
    }

    environment {
        // Définir des variables d'environnement si nécessaire
        PYTHONUNBUFFERED = '1'  // Pour éviter la mise en mémoire tampon de la sortie Python
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/morndiaye2007/flask-school-management.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install --upgrade pip'  // Mettre à jour pip
                sh 'pip install -r requirements.txt'  // Installer les dépendances du projet
                sh 'pip install pytest pytest-flask'  // Installer pytest et pytest-flask pour les tests
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --junitxml=test-results.xml'  // Exécuter les tests et générer un rapport JUnit
            }
            post {
                always {
                    junit 'test-results.xml'  // Publier les résultats des tests même en cas d'échec
                    archiveArtifacts artifacts: 'test-results.xml', allowEmptyArchive: true  // Archiver les résultats des tests
                }
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    gunicorn --bind 0.0.0.0:5000 run:app &  // Démarrer Gunicorn en arrière-plan
                    sleep 5  // Attendre que l'application démarre
                '''
            }
            post {
                success {
                    echo 'Application déployée avec succès sur http://localhost:5000'
                }
                failure {
                    echo 'Échec du déploiement de l\'application'
                }
            }
        }
    }

    post {
        always {
            cleanWs()  // Nettoyer l'espace de travail après l'exécution du pipeline
        }
    }
}