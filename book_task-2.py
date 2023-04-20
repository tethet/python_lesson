import sqlite3
import datetime

conn = sqlite3.connect('books.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS books
             (id INTEGER PRIMARY KEY,
              title TEXT,
              author TEXT,
              published_date TEXT,
              date_added TEXT,
              read INTEGER)''')

conn.commit()
conn.close()
