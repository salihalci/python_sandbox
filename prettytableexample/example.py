from prettytable import PrettyTable

table = PrettyTable()
#print(table)

table.add_column("İl",["Ankara","Adana","Eskişehir"])
table.add_column("Plaka",["06","01","26"])


table.align="l" #align left to all fields

print(table)