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

### Construction et démarrage des services
```bash
docker compose up --build -d