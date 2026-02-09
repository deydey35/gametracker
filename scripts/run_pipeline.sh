#!/bin/bash
set -e 

echo "1. Attente de la base..."
./scripts/wait-for-db.sh

echo "2. Initialisation SQL..."
mysql -h"$DB_HOST" -u"$DB_USER" -p"$DB_PASSWORD" "$DB_NAME" < scripts/init-db.sql

echo "3. Execution du pipeline ETL..."
python3 -m src.main

echo "4. Generation du rapport..."
# Le rapport est généré par le main ou un script dédié
echo "Terminé ! Verifiez le dossier output/"