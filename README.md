----
auteur : Aghilas OULD BRAHAM
----
<h3 align="center">TP : Programmation Distribué</h3>

<p align="center"><i>Cloud native</i></p>
<p align="center"
    <a href="https://www.u-paris.fr/">
       <img alt="Université Paris Cité" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Logo_Universit%C3%A9_Paris-Cit%C3%A9_%28partenariat_Wikim%C3%A9dia%29.svg/1024px-Logo_Universit%C3%A9_Paris-Cit%C3%A9_%28partenariat_Wikim%C3%A9dia%29.svg.png" width="100">
    </a>
</p>
<p align="center">
    <a href="https://docs.pypots.com/en/latest/install.html#reasons-of-version-limitations-on-dependencies">
       <img alt="Python version" src="https://img.shields.io/badge/Python-v3.12-E97040?logo=python&logoColor=white">
    </a>
    <a href="https://flask.palletsprojects.com/">
       <img alt="Flask version" src="https://img.shields.io/badge/Flask-v2.0.3-FF1493?logo=flask&logoColor=white">
    </a>
    <a href="https://www.docker.com/">
       <img alt="Docker version" src="https://img.shields.io/badge/Docker-v4.38.0-2496ED?logo=docker&logoColor=white">
    </a>
    <a href="https://kubernetes.io/">
       <img alt="Kubernetes version" src="https://img.shields.io/badge/Kubernetes-v1.21+-326CE5?logo=kubernetes&logoColor=white">
    </a>
</p>

----
# Creation du repository sur GitHub
* **En locale** :
````shell
mkdir TP # création du répértoire de travail
cd TP/ 

git init # initialiser TP/ comme depot git

# facultatives : Configurer le git
git config user.name "aghilas"
git config user.email "aghilasouldbraham8@gmail.com"

touch README.md # creation de ce fichier README

git add README.md  # ajouter le fichier au dépôt
git commit -m "commit init" # enregistrer les changements

# Soumission d'un dépôt existant par ligne de commande
git remote add origin https://github.com/Aghilas08/projet.git
git push -u origin master
````
* Lien 👉 : [depot github](https://github.com/Aghilas08/projet.git)

****
# Environnement Virtuel
Un environnement virtuel permet d'isoler les dépendances d'un projet Python des autres projets; Cela évite les conflits entre différentes versions de bibliothèques.
<U>**Remarque :**</U> utile pour ce TP car je vais utiliser **flask**(python) pour coder mes applications.
````shell
python -m venv mon_env # Créattion d'un environnement virtuel

cd mon_env/Scripts

.\activate # executer ce script afin d'activer l’environnement
````