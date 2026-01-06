import csv
import sqlite3

DB = "expense.db"
CSV_FILE = "sample_expenses.csv"

def create_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            description TEXT,
            amount REAL
        )
    """)

def seed():
    conn = sqlite3.connect(DB)
    create_table(conn)

    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = [(r["date"], r["category"], r["description"], float(r["amount"])) for r in reader]

    conn.executemany(
        "INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)",
        rows
    )
    conn.commit()
    conn.close()
    print(f"Seeded {len(rows)} rows into {DB}")

if __name__ == "__main__":
    seed()
