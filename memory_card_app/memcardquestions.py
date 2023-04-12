import sqlite3
"""
Created for memoryCards application. 
Responsible for bulk question insert operations to the table.
"""
#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('./memorycards.db')

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
(10,'What Azure powershell command for creating Web App?','New-AzWebApp'),
(11,'Benefits of API policies','Policies allow you to modify the behavior of the API using configuration instead of code. Policy can change both the inbound and outbound response.'),
(12,'.NET Framework class contains EventHubClient working with Event Hub','Microsoft.ServiceBus.Messaging'),
(13,'How can you configure regional maintenanca alert?','Azure Service Healt!'),
(14,'Create batch account command in CLI','az batch account create'),
(15,'What is strong consistency?','Strong consistency is that, across the world, readers are guaranteed to always get the most recent commited version of an item.'),
(16,'How can you prevent multiple processing an item in service bus queue?',"at-most-once -> en fazla bir defa"),
(17,'The API Gateway outbound policy allows you to change the output headers before sending to the client True/False','TRUE'),
(18,'What is the Cosmos DB storage capacity?','Unlimited'),
(19,'What do you need to link custom domain to Azure Service?','1 A Name 2 CName'),
(20,'AzCopy is the tool that can be used to copy large amounts of files between storage containers and accounts','TRUE'),
(21,'Difference between owner and contributer roles?',"Owner - Has full access to all resources including the right to delegate access to others. Contributor - Can create and manage all types of Azure resources but can't grant access to others."),
(22,'What is the limit of AKAMAI Content Delivery Vendor compare with Microsoft Premium','Does not support mobile rules'),
(23,'What is the Cosmos DB pricing elements?','1-Storage used in GB 2-Provisioned Request Unit per second (RU/s)'),
(24,'What do you need to use Azure AD?','1-Application ID 2-Redirect URL'),
(25,'ATP -Advanced Threat Protection will detect attempts to hack your SQL Database','TRUE'),
(26,'What do you need to use Azure AD?','1-Application ID 2-Redirect URL'),
(27,'SQL database can auto tune which features?','1-add new indexes, 2-remove unused indexes, 3-force the last good execution plan to be used'),
(28,'SQL Server Port','1433'),
(29,"What is the sample bash command for deploy and redeploy an Azure App Service?","az webapp up –location westeurope –name az204samplewebhtml –html"),
(30,"What is cmdlet and CLI command to create new slot?","New-AzWebAppSlot  / az webapp deployment slot create"),
(31,"What is the swap slot cmdlet command?","Invoke-AzResourceAction  /  az webapp deployment slot swap"),
(32,"BLOB Storage Tiers General Info?","""Hot tier - An online tier optimized for storing data that is accessed or modified frequently. The hot tier has the highest storage costs, but the lowest access costs.
Cool tier - An online tier optimized for storing data that is infrequently accessed or modified. Data in the cool tier should be stored for a minimum of 30 days. The cool tier has lower storage costs and higher access costs compared to the hot tier.
Archive tier - An offline tier optimized for storing data that is rarely accessed, and that has flexible latency requirements, on the order of hours. Data in the archive tier should be stored for a minimum of 180 days. """),
(33,"What is minimum pricing tier for Application service auto scale feture","Standard"),
(34,"WebApp deployment must reduce the likelihood of lockign files during deployment from CLI","Using a production and staging slot with auto swap enabled reduces the likelihood of locked files. run az webapp deploy to a staging slot with auto swap on"), 
(35,"What is the minimum plan for Microsoft Defener integration to Azure Functions","Anwe is Basic. Premium plan is also acceptable but expensive option. Consumption plan does not support Microsoft defener."),
(36,"The consistency level must maximize throughput and minimize latency for write operations.","Eventual consistency is correct option"),
(37,"Azure Cosmos change feed  by using a reactive model","1-Azure functions with an Azure Cosmos DB trigger. 2-Change feed processor library."),
(38,"Azure Cosmos DB ReadItemAsync method to read items async. Which two parameters do you need.","1- partitionkey, 2-item id"),
(39," * What are the change feed components",
 """1- The lease container component serves as a storage mechanism to manage state across multiple change feed consumers. 
 2-The delegate component is the code within the client application that implements business logic for each batch of changes.
 3-The host component is a client application instance that listens for changes from the change feed. 
 4-The monitored container component is monitored for any insert or update operations. """),
(40,"Blob content download code example retry mechanism codes","The code segment that includes options.Retry.MaxRetries = 10; and options.Retry.Delay = TimeSpan.FromSeconds(20); defines the retry strategy and downloads the content to the variable data.")
 
]

c.executemany("INSERT INTO questions VALUES(?,?,?)",questions_bulk)
print("Queries saved to database successfuly!")

#Commit our command
conn.commit()
conn.close()


#query database
#-----------------------------------
