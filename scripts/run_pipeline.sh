#!/bin/bash
set -e 

echo "1. Attente que MySQL soit prêt..."
./scripts/wait_for_db.sh

echo "2. Création des tables (init-db.sql)..."
mysql -h"$DB_HOST" -u"$DB_USER" -p"$DB_PASSWORD" "$DB_NAME" --skip-ssl < scripts/init-db.sql

echo "3. Lancement du pipeline ETL Python..."
python3 -m src.main

echo "4. Affichage du rapport final :"
echo "--------------------------------------------------"
cat output/rapport.txt
echo "--------------------------------------------------"