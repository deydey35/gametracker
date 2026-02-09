import pandas as pd
import numpy as np

def transform_players(df):
    df = df.copy()
    df = df.drop_duplicates(subset=['player_id']) 
    df['username'] = df['username'].str.strip() 
    df['registration_date'] = pd.to_datetime(df['registration_date'], errors='coerce') 
    # Nettoyage email : doit contenir '@' 
    df.loc[~df['email'].str.contains('@', na=False), 'email'] = None
    return df

def transform_scores(df, valid_player_ids): 
    df = df.copy()
    df = df.drop_duplicates(subset=['score_id']) 
    df['played_at'] = pd.to_datetime(df['played_at'], errors='coerce') 
    df['score'] = pd.to_numeric(df['score'], errors='coerce')
    # Supprimer scores <= 0 
    df = df[df['score'] > 0]
    # Supprimer références orphelines 
    df = df[df['player_id'].isin(valid_player_ids)]
    return df