import sqlite3

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')
#if db does not exist it will create it.

c=conn.cursor()

#create a table
c.execute("""CREATE TABLE customers (
    first_name TEXT,
    last_name TEXT,
    email TEXT
    )""")

#NULL
#INTEGER
#REAL
#TEXT
#BLOB

#Commit our command
conn.commit()
conn.close()
