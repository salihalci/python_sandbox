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
(1,'What two methods can you use to restrict public Internet access to a function app?','Removal of HTTP triggers. IP Access restriction'),
(2,'What is the maximum VM count in scale set?','1000'),
(3,'ISE Integration Service Environment','To run logic App on its own environment. -Their own hardware with no other customers.'),
(4,'What is the maximum apps in an App Service.','10'),
(5,'What is Data Collector API method?','Azure Monitor can collect data from any source with this API. Not just built in sources.'),
(6,'App Service Depoyment Options','1-Dropbox 2-Github 3-FTP 4- Portal is Wrong Answer!'),
(7,'What does App Service Environment ASE provide that an App Service Plan does not provide?','Fully isolated and dedicated environment.'),
(8,'What is the total maximum capacity of an unmanaged Azure Storage account in North America?','5PB'),
(9,'What is the maximum file size of block blob?','190.7 TB'),
(10,'What Azure powershell command for creating Web App?','New-AzWebApp')
]

c.executemany("INSERT INTO questions VALUES(?,?,?)",questions_bulk)
print("Queries saved to database successfuly!")

#Commit our command
conn.commit()
conn.close()


#query database
#-----------------------------------