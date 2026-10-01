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
        contribution_start_date TEXT
    )
    """)

    # Expenses
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        expense_date TEXT,
        expense_type TEXT,
        description TEXT,
        amount REAL NOT NULL
    )
    """)

    # Payments
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        member_id INTEGER NOT NULL,
        payment_date TEXT NOT NULL,
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


def add_member(
    full_name,
    contribution_start_date
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO members (
        full_name,
        contribution_start_date
    )
    VALUES (?, ?)
    """, (
        full_name,
        str(contribution_start_date)
    ))

    conn.commit()
    conn.close()

def get_members():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        full_name,
        contribution_start_date
    FROM members
    ORDER BY id
    """)

    records = cursor.fetchall()

    conn.close()

    return records


def update_member(member_id, full_name,contribution_start_date):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE members
    SET full_name = ?
        contribution_start_date = ?
    WHERE id = ?
    """, (full_name, str(contribution_start_date), member_id))

    conn.commit()
    conn.close()


def delete_member(member_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM members
    WHERE id = ?
    """, (member_id,))

    conn.commit()
    conn.close()


def add_expense(
    expense_date,
    expense_type,
    description,
    amount
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO expenses (
        expense_date,
        expense_type,
        description,
        amount
    )
    VALUES (?, ?, ?, ?)
    """, (
        str(expense_date),
        expense_type,
        description,
        amount
    ))

    conn.commit()
    conn.close()


def get_expenses():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        expense_date,
        expense_type,
        description,
        amount
    FROM expenses
    ORDER BY id
    """)

    records = cursor.fetchall()

    conn.close()

    return records


def update_expense(
    expense_id,
    expense_date,
    expense_type,
    description,
    amount
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE expenses
    SET
        expense_date = ?,
        expense_type = ?,
        description = ?,
        amount = ?
    WHERE id = ?
    """, (
        str(expense_date),
        expense_type,
        description,
        amount,
        expense_id
    ))

    conn.commit()
    conn.close()


def delete_expense(expense_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM expenses
    WHERE id = ?
    """, (expense_id,))

    conn.commit()
    conn.close()
def add_payment(
    member_id,
    payment_date,
    description,
    amount
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO payments (
        member_id,
        payment_date,
        description,
        amount
    )
    VALUES (?, ?, ?, ?)
    """, (
        member_id,
        str(payment_date),
        description,
        amount
    ))

    conn.commit()
    conn.close()


def get_payments():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        payments.id,
        payments.payment_date,
        members.full_name,
        payments.description,
        payments.amount
    FROM payments
    LEFT JOIN members
        ON payments.member_id = members.id
    ORDER BY payments.id
    """)

    records = cursor.fetchall()

    conn.close()

    return records


def update_payment(
    payment_id,
    member_id,
    payment_date,
    description,
    amount
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE payments
    SET
        member_id = ?,
        payment_date = ?,
        description = ?,
        amount = ?
    WHERE id = ?
    """, (
        member_id,
        str(payment_date),
        description,
        amount,
        payment_id
    ))

    conn.commit()
    conn.close()


def delete_payment(payment_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM payments
    WHERE id = ?
    """, (payment_id,))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
