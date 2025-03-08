#!/bin/bash
set -e

# Exécuter les migrations
flask db upgrade

# Lancer l'application Flask
exec python run.py