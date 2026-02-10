# 🎮 GameTracker - Pipeline ETL Automatisé

## Présentation du projet
GameTracker est une startup spécialisée dans l'analyse des performances des joueurs de jeux vidéo. Ce projet consiste à mettre en œuvre un pipeline **ETL** (Extract, Transform, Load) robuste et conteneurisé pour traiter des données brutes de profils de joueurs et de sessions de jeu.

L'objectif est de transformer des fichiers CSV "sales" en une base de données MySQL propre et d'en extraire un rapport de synthèse analytique automatique.

---

## Problèmes de qualité traités
Le pipeline détecte et corrige les **7 problèmes de qualité** identifiés dans les données sources:

1.  **Doublons** : Suppression des joueurs (basée sur le pseudo) et des scores (basée sur l'ID) apparaissant plusieurs fois.
2.  **Emails invalides** : Remplacement par `None` des adresses ne contenant pas de caractère `@`.
3.  **Dates incohérentes** : Normalisation des formats hétérogènes en dates valides (gestion des erreurs via `coerce`).
4.  **Espaces parasites** : Nettoyage des espaces superflus en début et fin de certains noms d'utilisateur.
5.  **Scores négatifs** : Suppression des sessions contenant des scores aberrants (négatifs ou nuls).
6.  **Valeurs manquantes** : Traitement des champs vides et conversion en `None` (NULL en SQL).
7.  **Références orphelines** : Suppression des scores faisant référence à un joueur non existant dans la liste nettoyée des profils.

---
## 📁 Structure du projet

```text
gametracker/
├── data/
│   └── raw/
│       ├── Players.csv
│       └── Scores.csv
├── output/                # Dossier des rapports générés
│   └── rapport.txt
├── scripts/               # Scripts d'automatisation et SQL
│   ├── init-db.sql
│   ├── run_pipeline.sh
│   └── wait-for-db.sh
├── src/                   # Code source Python (ETL)
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── extract.py
│   ├── load.py
│   ├── main.py
│   ├── report.py
│   └── transform.py
├── .gitignore             # Fichiers à ignorer par Git
├── docker-compose.yml     # Orchestration des services
├── Dockerfile             # Configuration de l'image application
├── README.md              # Documentation du projet
└── requirements.txt       # Dépendances Python

---
## Prérequis
- Docker et Docker Compose installés
- Accès réseau pour le build de l'image Python

## Construction et démarrage des services
```bash
docker compose up --build -d

Cette commande suffit à elle seule. C'est le bouton de démarrage qui permet d'orchestrer la mise en place de  l'environnement multi-services en une seule action.