import sqlite3
"""
Created for memory cards application.
Creates db tables.
"""
#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('./memorycards.db')
#if db does not exist it is going to create it.

c=conn.cursor()

#create a table
#c.execute("DROP TABLE QUESTIONS")
c.execute("""CREATE TABLE questions (
    id INTEGER,
    question TEXT,
    answer TEXT
    )""")
print("Memory cards db created successfuly!")
#NULL
#INTEGER
#REAL
#TEXT
#BLOB

#Commit our command
conn.commit()
conn.close()
