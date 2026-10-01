import sqlite3

DB_NAME = "family.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def initialize_database():

    conn = get_connection()
    cursor = conn.cursor()

    # Members
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        phone TEXT,
        email TEXT,
        status TEXT DEFAULT 'Active'
    )
    """)

    # Payments
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        member_id INTEGER,
        payment_date TEXT,
        description TEXT,
        amount REAL
    )
    """)

    # Levies
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS levies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        member_id INTEGER,
        levy_date TEXT,
        description TEXT,
        amount REAL
    )
    """)

    # Audit Log
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS audit_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action_date TEXT,
        action TEXT,
        details TEXT
    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    initialize_database()
