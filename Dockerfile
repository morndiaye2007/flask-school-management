# Utiliser une image Python légère
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .

# Copier les fichiers du projet dans le conteneur
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Rendre le script exécutable
RUN chmod +x entrypoint.sh

# Exposer le port utilisé par Flask (5000)
EXPOSE 5000

# Utiliser le script comme point d'entrée
ENTRYPOINT ["./entrypoint.sh"]