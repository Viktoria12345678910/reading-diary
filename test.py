import sqlite3
conn = sqlite3.connect('records.db')
c = conn.cursor()
c.execute("""DELETE FROM records""")
c.execute("""SELECT * FROM records """)
print(c.fetchall())