#!/bin/bash
set -e
MAX_TRIES=30
for i in $(seq 1 $MAX_TRIES); do
    if mysql -h"$DB_HOST" -u"$DB_USER" -p"$DB_PASSWORD" --skip-ssl -e "SELECT 1" > /dev/null 2>&1; then
        echo "Base de donnees prête !"
        exit 0
    fi
    echo "Tentative $i/$MAX_TRIES : Attente..."
    sleep 2
done
exit 1