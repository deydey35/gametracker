import pandas as pd

def load_data(df, table_name, conn):
    cursor = conn.cursor()
    # Gestion des NaN pour MySQL [cite: 129]
    df = df.replace({np.nan: None})
    
    cols = ", ".join(df.columns)
    placeholders = ", ".join(["%s"] * len(df.columns))
    updates = ", ".join([f"{c}=VALUES({c})" for c in df.columns if c != df.columns[0]])
    
    sql = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders}) ON DUPLICATE KEY UPDATE {updates}" 
    
    for _, row in df.iterrows():
        cursor.execute(sql, tuple(row))
    print(f"Chargé {len(df)} lignes dans {table_name}")