# Python for Everybody, Chapter 15 - Using Databases and SQL, Application 4

# Spidering Twitter using a database

import sqlite3

conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM People')
count = 0
print("People:")
for row in cur:
    if count < 5: print(row)
    count += 1

print(count, 'rows.')

cur.execute('SELECT * FROM Follows')
counter = 0
print("Follows:")
for row in cur:
    if counter < 5: print(row)
    counter += 1

print(counter, 'rows.')

cur.execute('''SELECT * FROM Follows JOIN People ON Follows.to_id = People.id WHERE Follows.id = 2''')

count = 0
print("Connections for id=2:")
for row in cur:
    if count < 5: print(row)
    count += 1

print(count, 'rows.')

cur.close()
