from app import create_app

# Créer l'application Flask
app = create_app()

if __name__ == '__main__':
    # Démarrer le serveur Flask
    app.run(host='0.0.0.0', port=5000, debug=True)