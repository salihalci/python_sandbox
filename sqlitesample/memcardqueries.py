import sqlite3

conn= sqlite3.connect("memorycards.db")

c = conn.cursor()

c.execute("SELECT * FROM questions")
#c.fetchone()
#c.fetchmany(3)
#c.fetchall()

#print(c.fetchall())

items = c.fetchall()

for x in items:
    print(f"{x[0]} Question {x[1]} ")

conn.commit()
conn.close()