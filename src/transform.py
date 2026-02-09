
import pandas as pd

def transform_players(df):
    """Nettoie les profils des joueurs"""
    df = df.copy()
    
    # 1. GESTION DES DOUBLONS (Problème n°1)
    # On nettoie d'abord les espaces pour bien comparer les noms
    df['username'] = df['username'].astype(str).str.strip() # Problème n°4
    
    # On supprime les doublons basés sur le nom d'utilisateur
    # On garde la première occurrence ('first')
    df = df.drop_duplicates(subset=['username'], keep='first') 
    
    # 2. AUTRES NETTOYAGES
    df['registration_date'] = pd.to_datetime(df['registration_date'], errors='coerce') # Problème n°3
    
    # Invalidation des emails sans @ (Problème n°2)
    df.loc[~df['email'].astype(str).str.contains('@', na=False), 'email'] = None 
    
    return df

def transform_scores(df: pd.DataFrame, valid_player_ids: list) -> pd.DataFrame:
    """Transforme et nettoie les donnees des scores.

    Args:
        df: DataFrame brut des scores.
        valid_player_ids: Liste des player_id valides.

    Returns:
        DataFrame nettoye.
    """
    df = df.copy()

    # Supprimer les doublons sur score_id
    df = df.drop_duplicates(subset=['score_id'])

    # Convertir les types numeriques appropriés
    if 'score' in df.columns:
        df['score'] = pd.to_numeric(df['score'], errors='coerce')
    
    if 'duration_minutes' in df.columns:
        df['duration_minutes'] = pd.to_numeric(df['duration_minutes'], errors='coerce')

    # Convertir played_at en datetime
    if 'played_at' in df.columns:
        df['played_at'] = pd.to_datetime(df['played_at'], errors='coerce')
        # Remplacer NaT par None
        df['played_at'] = df['played_at'].where(
            df['played_at'].notna(), None
        )

    # Supprimer les lignes avec un score negatif ou nul
    if 'score' in df.columns:
        df = df[df['score'] > 0]

    # Supprimer les scores dont le player_id n'est pas dans valid_player_ids
    if 'player_id' in df.columns:
        df = df[df['player_id'].isin(valid_player_ids)]

    # Remplacer NaN par None
    df = df.where(pd.notnull(df), None)

    print(f"Transforme {len(df)} scores")
    return df
