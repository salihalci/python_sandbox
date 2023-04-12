import sqlite3

conn= sqlite3.connect("./memorycards.db")

c = conn.cursor()

c.execute("SELECT * FROM questions")


items = c.fetchall()

for x in items:
     
    print(f"{x[0]} Question :'\n' {x[1]} ")
    print(f"{x[0]} Answer  :'\n' {x[2]} ")
    print("----------------------")
    
conn.commit()
conn.close()