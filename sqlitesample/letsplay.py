import sqlite3

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

#conn.execute("INSERT INTO customers VALUES('Deniz','Alcı','denizalci@gmail.com')")
#print("record inserted.")

many_customers=[('Ali','Kırmızı','alikirmizi@gmail.com')]




conn.commit()
conn.close()
