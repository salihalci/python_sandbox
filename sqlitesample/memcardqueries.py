import sqlite3

conn= sqlite3.connect("memorycards.db")

c = conn.cursor()

c.execute("SELECT * FROM questions")
#c.fetchone()
#c.fetchmany(3)
#c.fetchall()

print(c.fetchall())

conn.commit()
conn.close()