from app import create_app
from prometheus_client import start_http_server

# Créer l'application Flask
app = create_app()

if __name__ == '__main__':
    # Démarrer le serveur Prometheus sur le port 8000
    start_http_server(8000)

    # Démarrer l'application Flask sur le port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)