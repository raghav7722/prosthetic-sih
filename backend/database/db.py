
import sqlite3
from pathlib import Path


# Project root
BASE_DIR = Path(__file__).resolve().parents[2]

# Use the existing project database
DB_PATH = BASE_DIR / "data" / "gait_data.db"


def get_connection():
    """Return a connection to the existing gait database."""
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def check_database():
    """Check that the existing gait_data table is available."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table' AND name='gait_data'
    """)

    table = cursor.fetchone()
    connection.close()

    if table is None:
        raise RuntimeError("gait_data table does not exist.")

    return True


if __name__ == "__main__":
    check_database()
    print(f"Connected to: {DB_PATH}")
    print("gait_data table found successfully.")