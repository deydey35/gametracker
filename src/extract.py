import pandas as pd
import os

def extract(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Fichier manquant : {filepath}")
    df = pd.read_csv(filepath)
    print(f"Extrait : {len(df)} lignes de {os.path.basename(filepath)}") [cite: 111]
    return df