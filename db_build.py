import sqlite3
import csv

connect_db = sqlite3.connect('meditation.sql')

# create a sqlite3 database
cursor = connect_db.cursor()

# create a table    
cursor.execute('''CREATE TABLE IF NOT EXISTS meditation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book TEXT NOT NULL,
    content TEXT NOT NULL,
    language TEXT NOT NULL
)''')

# insert data into the table from a csv file
with open('meditation.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        cursor.execute('''INSERT INTO meditation (book, content, language) VALUES (?,?,?)''', row)

# commit changes    
connect_db.commit()

# close the connection
cursor.close()
f.close()
connect_db.close()

print('Done!')

