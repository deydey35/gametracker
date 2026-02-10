Voici le contenu complet de ton fichier **README.md**, nettoyé de toute citation et prêt à être utilisé pour ton rendu final.

---

# 🎮 GameTracker - Pipeline ETL Automatisé

## 📝 Présentation du projet

GameTracker est une startup spécialisée dans l'analyse des performances des joueurs de jeux vidéo. Ce projet consiste à mettre en œuvre un pipeline **ETL** (Extract, Transform, Load) robuste et conteneurisé pour traiter des données brutes de profils de joueurs et de sessions de jeu.

L'objectif est de transformer des fichiers CSV "sales" en une base de données MySQL propre et d'en extraire un rapport de synthèse analytique automatique.

---

## 🛠️ Problèmes de qualité traités

Le pipeline détecte et corrige les **7 problèmes de qualité** identifiés dans les données sources :

1. **Doublons** : Suppression des joueurs (via le pseudo) et des scores (via l'ID) apparaissant plusieurs fois.
2. **Emails invalides** : Identification et invalidation des adresses ne contenant pas de caractère `@`.
3. **Dates incohérentes** : Normalisation des formats variés (ISO, FR, etc.) via une conversion robuste.
4. **Espaces parasites** : Nettoyage des espaces en début et fin de certains noms d'utilisateur.
5. **Scores négatifs** : Suppression des scores aberrants (négatifs ou nuls).
6. **Valeurs manquantes** : Traitement des champs vides pour les emails ou les scores.
7. **Références orphelines** : Suppression des scores liés à un `player_id` inexistant dans le fichier des joueurs.

---

## 📁 Structure du projet

L'arborescence respecte l'organisation suivante pour garantir la modularité du code :

```text
gametracker/
├── data/
│   └── raw/               # Données brutes 
│       ├── Players.csv
│       └── Scores.csv
├── output/                # Dossier des rapports générés 
├── scripts/               # Scripts d'automatisation et SQL
│   ├── init-db.sql
│   ├── run_pipeline.sh
│   └── wait_for_db.sh
├── src/                   # Code source Python (ETL)
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── extract.py
│   ├── load.py
│   ├── main.py
│   ├── report.py
│   └── transform.py
├── .gitignore             # Fichiers exclus du versionnement
├── docker-compose.yml     # Orchestration des services MySQL et App
├── Dockerfile             # Configuration de l'image de l'application
├── README.md              # Documentation du projet
└── requirements.txt       # Dépendances Python 

```

---

## Prérequis

* Docker et Docker Compose installés et fonctionnels.
* Accès réseau pour la construction (build) de l'image Python.

---

## Construction et démarrage des services

Pour lancer l'intégralité du pipeline, exécutez la commande suivante à la racine du projet :

```bash
docker compose up --build -d

```

### 🔍 Détails de l'automatisation

Cette commande suffit à elle seule pour piloter le projet. C'est le "bouton de démarrage" qui permet d'orchestrer la mise en place de l'environnement multi-services en une seule action :

1. **Build** : Elle construit l'image de l'application en installant le client MySQL et les dépendances Python.
2. **Orchestration** : Elle démarre la base de données et attend qu'elle soit opérationnelle (`service_healthy`) avant de lancer l'application.
3. **Exécution automatique** : Une fois lancée, elle déclenche le script `run_pipeline.sh` qui initialise les tables SQL, exécute le pipeline ETL Python et génère le rapport final dans `output/rapport.txt`.

