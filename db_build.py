import sqlite3
import csv

connect_db = sqlite3.connect('marcus.db')

# create a sqlite3 database
cursor = connect_db.cursor()

# create a table    
cursor.execute('''CREATE TABLE IF NOT EXISTS meditation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book TEXT NOT NULL,
    chapter TEXT NOT NULL,
    content TEXT NOT NULL,
    language TEXT NOT NULL
)''')

# insert data into the table from a csv file
with open('meditations.csv', 'r') as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        cursor.execute('''INSERT INTO meditation (book, chapter, content, language) VALUES (?,?,?,?)''', row)

# commit changes    
connect_db.commit()

# close the connection
cursor.close()
f.close()
connect_db.close()

# Create a new connection & cursor
new_connect = sqlite3.connect("marcus.db")
new_cursor = new_connect.cursor()

# Get the data
res = new_cursor.execute('''SELECT content FROM meditation''')
res.fetchall()

# Print the data
for row in res:
    print(row)

# close the connection
new_cursor.close()
new_connect.close()

print('Done!')

