# Python for Everybody, Chapter 15 - Using Databases and SQL, Application 2

# Querying Your Twitter Database

import sqlite3

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()
cur.execute('SELECT * FROM Twitter')
count = 0
for row in cur:
    print(row)
    count += 1

print(count, 'rows.')
cur.close()
