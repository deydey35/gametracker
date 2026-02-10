#!/bin/bash
set -e 

echo "1. Attente de la base de données..."
./scripts/wait-for-db.sh

echo "2. Initialisation des tables SQL..."
mysql -h"$DB_HOST" -u"$DB_USER" -p"$DB_PASSWORD" "$DB_NAME" < scripts/init-db.sql

echo "3. Exécution du pipeline ETL (Extraction, Transformation, Nettoyage)..."
python3 -m src.main

echo "4. Affichage du rapport final :"
echo "--------------------------------------------------"

cat output/rapport.txt
echo "--------------------------------------------------"

echo "Traitement terminé avec succès !"