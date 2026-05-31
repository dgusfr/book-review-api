import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "src" / "schema.db"


with sqlite3.connect(DB_PATH) as connection:
    cursor = connection.cursor()
    cursor.executemany(
        "INSERT INTO users (username) VALUES (?)",
        [
            ("João",),
            ("Maria",),
            ("Pedro",),
        ],
    )
    connection.commit()

print("3 usuarios inseridos com sucesso.")
