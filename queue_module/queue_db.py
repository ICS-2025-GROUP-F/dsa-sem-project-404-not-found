import sqlite3

DB_NAME = 'queue_db.sqlite3'

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_table():

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passengers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            ticket_number TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

def insert_passenger(name, ticket_number):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO passengers (name, ticket_number)
        VALUES (?, ?)
    ''', (name, ticket_number))
    conn.commit()
    conn.close()

def fetch_all_passengers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT name, ticket_number FROM passengers ORDER BY id ASC')
    rows = cursor.fetchall()
    conn.close()
    return [{"name": row[0], "ticket_number": row[1]} for row in rows]

def delete_passenger_by_ticket(ticket_number):

   conn =get_connection()
   cursor = conn.cursor()
   cursor.execute('DELETE FROM passengers WHERE ticket_number = ? ',(ticket_number,))
   conn.commit()
   conn.close()