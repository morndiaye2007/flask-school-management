#!/bin/bash
set -e

# Démarrer le serveur Prometheus pour les métriques sur le port 8000
python -m prometheus_client &

# Exécuter les migrations de base de données
flask db upgrade

# Lancer l'application Flask
exec python run.py