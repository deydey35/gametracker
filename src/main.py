from src.config import Config
from src.extract import extract
from src.transform import transform_players, transform_scores
from src.load import load_data
from src.database import database_connection
from src.report import generate_report

def main():
    with database_connection() as conn:
        # 1. Players
        df_p = extract(f"{Config.DATA_DIR}/Players.csv")
        df_p_clean = transform_players(df_p)
        load_data(df_p_clean, "players", conn)
        
        # 2. Scores
        valid_ids = df_p_clean['player_id'].tolist() 
        df_s = extract(f"{Config.DATA_DIR}/Scores.csv")
        df_s_clean = transform_scores(df_s, valid_ids)
        load_data(df_s_clean, "scores", conn)
        
    generate_report()

if __name__ == "__main__":
    main()