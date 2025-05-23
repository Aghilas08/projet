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
<U>**Remarque :**</U> utile pour ce TP car je vais utiliser **flask**(python) pour coder mon application.
````shell
python -m venv mon_env # Créattion d'un environnement virtuel
cd mon_env/Scripts
.\activate # executer ce script afin d'activer l’environnement
````

****

# MicroService
👉 [app.py](app.py)
## 1- Présentation
Le microservice "product_service" est une application web développée en Python avec Flask. Elle gère une liste de produits et permet aux utilisateurs d'ajouter et de consulter ces produits via des requêtes HTTP.

### Fonctionnalité
Ce microservice expose deux routes principales :
* **Route d'accueil ("/")**
  * Méthode : **GET** : Affiche un message de bienvenue avec un lien vers la liste des produits.

* **Route de gestion des produits ("/product")**
   *  Méthode **GET** : Retourne la liste des produits sous format JSON.
   *  Méthode **POST** : Permet d'ajouter un produit à la liste. Les données sont envoyées en JSON dans le corps de la requête.

<U>**Remarque :**</U> Pour mon premier teste en locale y a aucune donnée.

### Teste en locale
![Acceuil](./img/home.png)

![product_list0](./img/product000.png)

* **log** : ``127.0.0.1 - - [13/Mar/2025 00:49:59] "GET / HTTP/1.1" 200 -``
  * indique qu'une requête GET a été reçue et traitée avec succès (200).

## 2- Postman
**Postman** est un outil qui permet de tester et d’interagir avec des API. Il facilite l’envoi de requêtes HTTP (GET, POST, PUT, DELETE) et l’affichage des réponses.

![pstman](./img/postman.png)

* **Configurer la requête**
   *  **URL** : 127.0.0.1:5000/product
   *  **Body** puis sélectionner **raw** et choisir **JSON**.

* **Résultat :**

![product_list001](./img/product001.png)

* **log** : ``127.0.0.1 - - [13/Mar/2025 23:14:59] "POST /product HTTP/1.1" 200 -``
  * Ce message indique que le serveur a bien reçu et traité une requête POST sur /product avec succès (200)

## 3- Ajout de données

````python
product = [    
    {"id": 1, "name": "PC", "price": 1200},
    {"id": 2, "name": "SAMSUNG S24", "price": 1300}
]
````
****

# Docker

![docker](./img/docker1.png)

## 1- Dockerfile
Le code source est interprété au moment de l’exécution. Cela signifie que pour exécuter une application Python, on a besoin de :
*  L’interpréteur Python
*  Les fichiers source .py
*  Les dépendances (ex: Flask, requests, etc...)
*  Avantages de convertir le code Python en un binaire (exécutable) avant de le dockeriser :
   *  Portabilité
   *  Réduction de la taille de l’image Docker

👉 [Dockerfile](Dockerfile)

## 2- Gestion des dépendances

Le fichier **requirements.txt** est utilisé pour lister toutes les dépendances nécessaires pour réliser ce TP.

👉 [requirements](requirements.txt)

## 3- Creation de l'image doker
* se positioner dans **TP/**
* executer : ``docker build -t product_service . ``
* Afficher les images docker : ``docker images``

![docker_container](./img/container.png)

* lancer en locale : ``docker run --name "my_app" -p 8080:5000 product_service``

* **Résultat :**

![run_app](./img/run_app.png)

## 4- Publier l'image docker

Lien 👉 : [Docker Hub](https://hub.docker.com/repository/docker/aghilasob/product_app/general)

permet de stocker, partager des **images Docker**. Il sert principalement à :

* **Stocker des images Docker**
* **Partager des images :** Il permet de collaborer en partageant des images via des dépôts publics ou privés.
* **Automatiser les builds :** peut automatiquement construire des images à partir d'un dépôt *GitHub*.
* **Distribuer des conteneurs :** Les développeurs peuvent facilement tirer faire des **pull** et des **push** des images vers et depuis Docker Hub.
**Accéder aux images officielles**

###### Tag l'image docker :
*  ``docker tag imageID yourDockerHubName/imageName:version``

````sh
sudo docker tag 434b2108b89b aghilasob/product_app:01
````

###### Login docker hub :
* ``docker login``

````sh
$ docker login
username : 
password :
````

###### Pousser l'image vers docker hub : 
* ``docker push yourDockerHubName/imageName:version``

````sh
$ docker push aghilasob/product_app:01
````


![docker_hub](./img/docker_hub.png)

****
# Programme teste

👉 [test_app](test_app.py)

L'utilisation de tests dans le développement d'une application, comme mon service Flask, est essentielle pour plusieurs raisons :
* **Garantir le bon fonctionnement de l'application :** Vérifier que la route **/product** retourne bien une liste de produits.
* **Automatiser les vérifications (CI/CD) :** Les tests sont souvent intégrés dans des pipelines CI/CD (GitHub Actions,etc.), ce qui permet :
   *  De valider le code avant chaque déploiement
   *  D’éviter les erreurs en production

# Pipline CI/CD

👉 [action](.github\workflows\action.yml)

###### Teste :

![teste](./img/git.png)

###### pull request :

![pull_req](./img/git_teste.png)

* **Récuperer la nouvelle version :** ``git pull origin master``
  
****
# Dépoloiment

👉 [deployment](deployment.yml)

### Minikube
````sh
minikube start --driver=docker
minikube dashboard
````
### Deployer le service product 
````sh
kubectl apply -f deployment.yml
````

* **Verification :**

![dep_service](/img/deploymnt.png)

* **Lancer le service :**
````sh
minikube service product-service
````

![teste](/img/test_dep.png)

****

# Mettre en place une Gateway

**Linge 37 ::** 👉 [deployment](deployment.yml)

````
en utilisant istio
        |\          
        | \         
        |  \        
        |   \       
      /||    \      
     / ||     \     
    /  ||      \    
   /   ||       \   
  /    ||        \  
 /     ||         \ 
/______||__________\
____________________
  \__       _____/  
     \_____/        

# Installation :

curl -L https://istio.io/downloadIstio | sh -
cd istio-1.25.2
export PATH=$PWD/bin:$PATH 
istioctl install --set profile=demo -y 
````

* **Appliquer la configuration :**
````sh
kubectl apply -f deployment.yml
````      
* **Obtenir l’adresse IP externe :**
````sh
kubectl get svc istio-ingressgateway -n istio-system
````

![gw](/img/gw.png)

****

# Teste

* ``kubectl -n istio-system port-forward svc/istio-ingressgateway 8080:80``

![ports](/img/ports.png)

* **Teste via le navigateur :**

````
http://localhost:8080/
http://localhost:8080/produc
````

![teste_navigateur](/img/navigateur.png)

****

# Grafana

* **s'assurer d'abord d'ajouters les addons :** ``istioctl install --set profile=demo -y``
  
* **l'activer :** 
````
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.20/samples/addons/grafana.yaml

kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.20/samples/addons/prometheus.yaml
````

* **Acceder a Grafana en local :**``kubectl port-forward -n istio-system svc/grafana 3000:3000``
   *  **via :** http://localhost:3000


![grafana_perf](/img/perf.png)

# FIN
****