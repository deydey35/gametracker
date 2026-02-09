import pandas as pd
import os

def extract(filepath):
    """Lit un CSV et affiche le nombre de lignes extraites."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Erreur : Le fichier {filepath} est introuvable.")
    
    df = pd.read_csv(filepath)
    print(f"Extraction reussie : {len(df)} lignes lues depuis {os.path.basename(filepath)}.")
    return df