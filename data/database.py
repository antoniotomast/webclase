import mysql.connector 
import os

# Configuración para Docker o local
DB_HOST = os.getenv('DB_HOST', 'mysql')  # 'mysql' es el nombre del servicio en docker-compose
DB_PORT = int(os.getenv('DB_PORT', 3306))
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'root')
DB_NAME = os.getenv('DB_NAME', 'oscar')

database = mysql.connector.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME,
    ssl_disabled=True
) 