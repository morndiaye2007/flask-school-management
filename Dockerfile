# Utiliser une image Python légère
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier les fichiers du projet dans le conteneur
COPY . .

# Rendre le script exécutable
RUN chmod +x entrypoint.sh

# Exposer les ports utilisés par Flask (5000) et Prometheus (8000)
EXPOSE 5000 8000

# Utiliser le script comme point d'entrée
ENTRYPOINT ["./entrypoint.sh"]