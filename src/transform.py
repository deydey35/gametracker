
import pandas as pd

def transform_players(df: pd.DataFrame) -> pd.DataFrame:
    """Transforme et nettoie les donnees des joueurs.

    Args:
        df: DataFrame brut des joueurs.

    Returns:
        DataFrame nettoye.
    """
    df = df.copy()

    # Supprimer les doublons sur player_id
    df = df.drop_duplicates(subset=['player_id'])

    # Nettoyer les espaces des username (strip)
    if 'username' in df.columns:
        df['username'] = df['username'].str.strip()

    # Convertir les dates d'inscription
    if 'registration_date' in df.columns:
        df['registration_date'] = pd.to_datetime(df['registration_date'], errors='coerce')
        # Remplacer NaT par None pour MySQL
        df['registration_date'] = df['registration_date'].where(
            df['registration_date'].notna(), None
        )

    # Nettoyer les emails invalides (sans @)
    if 'email' in df.columns:
        df['email'] = df['email'].where(
            df['email'].str.contains('@', na=False), None
        )
    
    # Remplacer NaN par None pour les autres colonnes si besoin
    df = df.where(pd.notnull(df), None)

    print(f"Transforme {len(df)} joueurs")
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
