import mysql.connector
import time
from contextlib import contextmanager
from src.config import Config

def get_connection():
    """Crée une connexion simple à la base de données MySQL."""
    return mysql.connector.connect(
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        database=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD
    )

def get_connection_with_retry(max_retries=5, delay=2):
    """Tente de se connecter plusieurs fois avant d'abandonner."""
    for attempt in range(max_retries):
        try:
            return get_connection()
        except Exception as e:
            print(f"Tentative {attempt + 1}/{max_retries}: {e}")
            if attempt < max_retries - 1:
                time.sleep(delay)
    raise Exception("Impossible de se connecter à la base.")

@contextmanager
def database_connection():
    """Gère l'ouverture, le commit et la fermeture automatique."""
    conn = get_connection_with_retry()
    try:
        yield conn
        conn.commit()  
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()