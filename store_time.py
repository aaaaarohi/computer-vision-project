import sqlite3
from read_text import*
from store_time import*

number_plate=extracted_text

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("vehicles.db")
cursor = conn.cursor()

# Create a table for storing vehicle number plates
cursor.execute('''
    CREATE TABLE IF NOT EXISTS vehicles (
        number_plate TEXT PRIMARY KEY,
        in_time TEXT,
        out_time TEXT
    )
''')

cursor.execute("INSERT INTO vehicles (number_plate) VALUES (?)", (number_plate,))
cursor.execute("INSERT INTO vehicles (in_time) VALUES (?)", (detection_time,))



# Commit and close connection
conn.commit()
conn.close()
