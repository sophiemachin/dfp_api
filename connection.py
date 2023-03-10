import psycopg2
import os

connection_details = {
    "host": os.environ.get('HOST'),
    "dbname": os.environ.get('DB_NAME'),
    "user": os.environ.get('USER'),
    "password": os.environ.get('PASSWORD'),
}


def connect_to_db():
    conn = psycopg2.connect(**connection_details)
    cursor = conn.cursor()
    return cursor, conn


