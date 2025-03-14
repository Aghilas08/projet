# image python comme interpreteur
FROM python:3 

# rep de travail
WORKDIR /app

COPY . /app

# Installer les dépendances depuis requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4000 

# Lancer l'app
CMD ["python", "app.py"]