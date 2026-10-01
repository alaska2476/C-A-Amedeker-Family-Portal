import sqlite3

def initialize_database():

    conn = sqlite3.connect("family.db")
    cursor = conn.cursor()
    
    # Members
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        phone TEXT,
        email TEXT
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
