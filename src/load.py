import pandas as pd
import numpy as np

def load_data(df, table_name, conn):
    """Charge les donnees avec gestion des valeurs manquantes."""
    cursor = conn.cursor()
    # Remplacement des NaN par None pour MySQL 
    df_sql = df.replace({np.nan: None})
    print(df_sql)
    cols = ", ".join(df_sql.columns)
    placeholders = ", ".join(["%s"] * len(df_sql.columns))
    updates = ", ".join([f"{c}=VALUES({c})" for c in df_sql.columns[1:]])
    
    query = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders}) ON DUPLICATE KEY UPDATE {updates}"
    
    for _, row in df_sql.iterrows():
        cursor.execute(query, tuple(row))
    print(f"Chargement termine : {len(df_sql)} lignes inserees dans {table_name}.")