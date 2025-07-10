import sqlite3

DB_NAME = 'stack_db.sqlite3'

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS stack_passengers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    ticket_number TEXT NOT NULL UNIQUE
    )
    ''')
    conn.commit()
    conn.close()

def insert_passenger(name, ticket_number):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
           INSERT INTO stack_passengers (name, ticket_number)
           VALUES (?, ?)
        ''', (name, ticket_number))
        conn.commit()
    except sqlite3.IntegrityError:
        raise ValueError(f"Ticket number {ticket_number} already exists.")
    finally:
        conn.close()

def fetch_all_passengers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT name, ticket_number FROM stack_passengers ORDER BY id ASC')
    rows = cursor.fetchall()
    conn.close()
    return [{"name": row[0], "ticket_number": row[1]} for row in rows]

def delete_passenger_by_ticket(ticket_number):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM stack_passengers WHERE ticket_number = ?', (ticket_number,))
    conn.commit()
    conn.close()