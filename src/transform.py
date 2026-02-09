import pandas as pd

def transform_players(df):
    """Nettoie les profils des joueurs"""
    df = df.copy()
    df = df.drop_duplicates(subset=['player_id'])  
    df['username'] = df['username'].astype(str).str.strip() 
    df['registration_date'] = pd.to_datetime(df['registration_date'], errors='coerce')  
    # Invalidation des emails sans @ 
    df.loc[~df['email'].astype(str).str.contains('@', na=False), 'email'] = None 
    return df

def transform_scores(df, valid_player_ids):
    """Nettoie les sessions de jeu et filtre les orphelins."""
    df = df.copy()
    df = df.drop_duplicates(subset=['score_id']) 
    df['score'] = pd.to_numeric(df['score'], errors='coerce')
    df = df[df['score'] > 0] 
    df['played_at'] = pd.to_datetime(df['played_at'], errors='coerce') 
    # Suppression des references orphelines 
    df = df[df['player_id'].isin(valid_player_ids)] 
    return df