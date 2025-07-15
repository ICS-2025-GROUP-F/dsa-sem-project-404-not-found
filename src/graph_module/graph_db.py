import sqlite3
DB_NAME = 'graph_db.sqlite3'

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Passenger table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS graph_passengers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            ticket_number TEXT NOT NULL UNIQUE
        )
    ''')

    # Graph connections table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS graph_connections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_ticket TEXT NOT NULL,
            to_ticket TEXT NOT NULL,
            FOREIGN KEY(from_ticket) REFERENCES graph_passengers(ticket_number),
            FOREIGN KEY(to_ticket) REFERENCES graph_passengers(ticket_number)
        )
    ''')

    conn.commit()
    conn.close()

def insert_passenger(name, ticket_number):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO graph_passengers (name, ticket_number)
        VALUES (?, ?)
    ''', (name, ticket_number))
    conn.commit()
    conn.close()

def insert_connection(from_ticket, to_ticket):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO graph_connections (from_ticket, to_ticket)
        VALUES (?, ?)
    ''', (from_ticket, to_ticket))
    conn.commit()
    conn.close()

def fetch_all_passengers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT name, ticket_number FROM graph_passengers ORDER BY id ASC')
    rows = cursor.fetchall()
    conn.close()
    return [{"name": row[0], "ticket_number": row[1]} for row in rows]

def fetch_all_connections():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT from_ticket, to_ticket FROM graph_connections')
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_passenger_by_ticket(ticket_number):
    conn = get_connection()
    cursor = conn.cursor()
    # Delete passenger and all related connections
    cursor.execute('DELETE FROM graph_passengers WHERE ticket_number = ?', (ticket_number,))
    cursor.execute('DELETE FROM graph_connections WHERE from_ticket = ? OR to_ticket = ?', (ticket_number, ticket_number))
    conn.commit()
    conn.close()
