from src.database import database_connection
from datetime import datetime

def generate_report():
    with database_connection() as conn:
        cursor = conn.cursor()
        with open("output/rapport.txt", "w") as f: 
            f.write("====== GAMETRACKER ======\n")
            f.write(f"Rapport généré le {datetime.now()}\n\n")
            
            # 1. Stats générales 
            cursor.execute("SELECT COUNT(*) FROM players")
            f.write(f"Nombre de joueurs : {cursor.fetchone()[0]}\n")
            cursor.execute("SELECT COUNT(*) FROM scores")
            f.write(f"Nombre de scores : {cursor.fetchone()[0]}\n\n")
            
            # 2. Top 5 
            f.write("Top 5 Meilleurs Scores :\n")
            cursor.execute("""
                SELECT p.username, s.game, s.score 
                FROM scores s JOIN players p ON s.player_id = p.player_id 
                ORDER BY s.score DESC LIMIT 5
            """)
            for row in cursor.fetchall():
                f.write(f"{row[0]} | {row[1]} | {row[2]}\n")