import os
from datetime import datetime
from src.database import database_connection

def generate_report():
    """Génère un rapport de synthèse complet et professionnel dans le dossier output."""
    
    # Création sécurisée du dossier de sortie
    os.makedirs("output", exist_ok=True)
    
    with database_connection() as conn:
        cursor = conn.cursor()
        
        with open("output/rapport.txt", "w", encoding="utf-8") as f:
            # --- ENTÊTE ---
            f.write("="*50 + "\n")
            f.write(" " * 15 + "GAMETRACKER - RAPPORT ANALYTIQUE\n")
            f.write("="*50 + "\n")
            f.write(f"Date de génération : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
            f.write("-" * 50 + "\n\n")

            # 1. STATISTIQUES GLOBALES
            f.write("### 1. VUE D'ENSEMBLE DES DONNÉES\n")
            cursor.execute("SELECT COUNT(*) FROM players")
            total_players = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM scores")
            total_scores = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(DISTINCT game) FROM scores")
            total_games = cursor.fetchone()[0]
            
            f.write(f" • Nombre total de joueurs uniques  : {total_players}\n")
            f.write(f" • Nombre total de sessions de jeu  : {total_scores}\n")
            f.write(f" • Nombre de titres différents      : {total_games}\n\n")

            # 2. PANTHÉON DES SCORES (TOP 5)
            f.write("### 2. TOP 5 DES MEILLEURS SCORES\n")
            f.write(f"{'Pseudo':<20} | {'Jeu':<15} | {'Score':<10}\n")
            f.write("-" * 50 + "\n")
            cursor.execute("""
                SELECT p.username, s.game, s.score 
                FROM scores s 
                JOIN players p ON s.player_id = p.player_id 
                ORDER BY s.score DESC LIMIT 5
            """)
            for (user, game, score) in cursor.fetchall():
                f.write(f"{user:<20} | {game:<15} | {score:<10}\n")
            f.write("\n")

            # 3. PERFORMANCE PAR JEU
            f.write("### 3. SCORE MOYEN PAR JEU\n")
            cursor.execute("SELECT game, ROUND(AVG(score), 2) FROM scores GROUP BY game ORDER BY AVG(score) DESC")
            for (game, avg_score) in cursor.fetchall():
                f.write(f" • {game:<15} : {avg_score:>10} pts\n")
            f.write("\n")

            # 4. RÉPARTITION GÉOGRAPHIQUE
            f.write("### 4. TOP 3 DES PAYS (JOUEURS)\n")
            cursor.execute("SELECT country, COUNT(*) FROM players GROUP BY country ORDER BY COUNT(*) DESC LIMIT 3")
            for (country, count) in cursor.fetchall():
                f.write(f" • {country:<15} : {count} joueur(s)\n")
            f.write("\n")

            # 5. ANALYSE DES PLATEFORMES
            f.write("### 5. UTILISATION DES PLATEFORMES\n")
            cursor.execute("SELECT platform, COUNT(*) FROM scores GROUP BY platform ORDER BY COUNT(*) DESC")
            for (plat, count) in cursor.fetchall():
                f.write(f" • {plat:<15} : {count} sessions\n")
            
            f.write("\n" + "="*50 + "\n")
            f.write(" " * 18 + "FIN DU RAPPORT\n")
            f.write("="*50 + "\n")

    print("Succès : Rapport analytique 'output/rapport.txt' généré.")