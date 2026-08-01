import sqlite3
from config import Config


def get_connection():
    """
    Create and return a SQLite database connection.
    """
    conn = sqlite3.connect(Config.DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def close_connection(conn):
    """
    Close the database connection.
    """
    if conn:
        conn.close()