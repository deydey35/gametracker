import os

class Config:
    DB_HOST = os.environ.get('DB_HOST', 'db')
    DB_PORT = int(os.environ.get('DB_PORT', 3306)) 
    DB_NAME = os.environ.get('DB_NAME', 'gametracker_db')
    DB_USER = os.environ.get('DB_USER', 'user_gt')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'pass_gt')
    DATA_DIR = "/app/data/raw"