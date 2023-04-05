import sqlite3
"""
Created for memoryCards application. 
Responsible for bulk question insert operations to the table.
"""
#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('memorycards.db')

#if db does not exist it will create it.

c=conn.cursor()
#conn.execute("INSERT INTO customers VALUES('Deniz','Alcı','denizalci@gmail.com')")
#print("record inserted.")

#TODO bulk questions going to be loaded from a database or file
questions_bulk = [
    (1,'Sample Question','Sample Answer'),
    (2,'Sample Question2','Sample Answer2')
]

c.executemany("INSERT INTO questions VALUES(?,?,?)",questions_bulk)
print("Queries saved to database successfuly!")

#Commit our command
conn.commit()
conn.close()


#query database
#-----------------------------------