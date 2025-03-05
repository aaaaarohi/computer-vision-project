import sqlite3
import datetime
from read_text import*
from store_time import*
from car_detection import*

number_plate=extracted_text

if is_detected:
    detection_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("vehicles.db")
cursor = conn.cursor()


cursor.execute("INSERT INTO vehicles (number_plate) VALUES (?)", (number_plate,))
cursor.execute("INSERT INTO vehicles (in_time) VALUES (?)", (detection_time,))



# Commit and close connection
conn.commit()
conn.close()
