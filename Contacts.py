import sqlite3


# Function to create the table if not exists
def create_table():
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            CellNumber TEXT NOT NULL,
            Email TEXT
        )
    ''')

    connection.commit()
    connection.close()


# Function to insert data into the table
def insert_data(name, cell_number, email):
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO contacts (Name, CellNumber, Email) VALUES (?, ?, ?)
    ''', (name, cell_number, email))

    connection.commit()
    connection.close()


# Function to fetch all data from the table and display them
def fetch_and_display_data():
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM contacts
    ''')

    data = cursor.fetchall()

    for row in data:
        print(f"ID: {row[0]}, Name: {row[1]}, Cell#: {row[2]}, Email: {row[3]}")

    connection.close()


# Create table if not exists
create_table()

# Insert 5 rows of data
insert_data("Navya", "1234567890", "navz@example.com")
insert_data("Prashanth", "9876543210", "prash@example.com")
insert_data("Muskan", "5555555555", "mus@example.com")
insert_data("Harsh", "7777777777", "har@example.com")
insert_data("Asmatha", "9999999999", "asz@example.com")

# Fetch and display all data
fetch_and_display_data()