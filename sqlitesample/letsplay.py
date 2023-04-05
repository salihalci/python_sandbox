import sqlite3

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

#conn.execute("INSERT INTO customers VALUES('Deniz','Alcı','denizalci@gmail.com')")
#print("record inserted.")

many_customers=[('Ali','Kırmızı','alikirmizi@gmail.com')]




conn.commit()
conn.close()
import sqlite3

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')
#if db does not exist it will create it.

c=conn.cursor()

many_customers = [
    ('Orhan','Polat','orhanpolat@gmail.com'),
    ('Gokmen','Doğutürk','gokmendoguturk@gmail.com')
]

c.executemany("INSERT INTO CUSTOMERS VALUES(?,?,?)",many_customers)
print("many customers inserted successfully!")

#Commit our command
conn.commit()
conn.close()
