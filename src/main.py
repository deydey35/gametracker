"""Point d'entree du pipeline ETL."""
import sys
from src.config import Config
from src.database import database_connection
from src.extract import extract
from src.transform import transform_players, transform_scores
from src.load import load_players, load_scores
from src.report import generate_report

def run_pipeline():
    """Execute le pipeline ETL complet."""
    print("=" * 50)
    print("Demarrage du pipeline ETL")
    print("=" * 50)

    try:
        with database_connection() as conn:
            # ETL Players
            print("\n--- Traitement des Players ---")
            df_players = extract(f"{Config.DATA_DIR}/Players.csv")
            df_players = transform_players(df_players)
            load_players(df_players, conn)

            # Get valid player_ids for scores cleaning
            valid_player_ids = df_players['player_id'].tolist()
            
            # ETL Scores
            print("\n--- Traitement des Scores ---")
            df_scores = extract(f"{Config.DATA_DIR}/Scores.csv")
            df_scores = transform_scores(df_scores, valid_player_ids)
            load_scores(df_scores, conn)
            
        print("\n" + "=" * 50)
        print("Pipeline ETL termine avec succes!")
        print("=" * 50)
        
        # Generation du rapport
        print("\n--- Generation du rapport ---")
        generate_report()
            
    except Exception as e:
        print(f"\nErreur critique dans le pipeline: {e}")
        sys.exit(1)

if __name__ == '__main__':
    run_pipeline()