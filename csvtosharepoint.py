import csv
import pandas as pd
import prettytable


rows = []
header = ['Barcode','Bedrijf','Datum toegekomen','Ordernummer','Klant','Ref','Lengte','Transport','Opmerkingen','Status','Datum ingescand','','','']
with open(r"\\192.168.0.100\scanimport\Master\Stock.csv") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        splitted_row = row[0].split(';')
        rows.append(splitted_row)
with open(r"\\192.168.0.100\scanimport\Master\test.csv",'r+') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for row in rows:
        writer.writerow(row)

   
csvreadernewfile = open(r"\\192.168.0.100\scanimport\Master\test.csv" ,'r', encoding= 'ANSI')
data = csvreadernewfile.readlines()
column_names = data[0].split(',')
print(column_names)
table = prettytable.PrettyTable()
table.add_row(column_names)
print(table)
print(len(data[2000].split(',')))
print(len(data))
for i in range(len(data)-2,2,-2):
    print(i)
    print(len(data[i]))
    if len(data[i]) > 14:    
        del data[-3]
    splitted_data = data[i].split(',')
    if len(splitted_data) <14:
        for i in range(0,14-len(splitted_data)):
            splitted_data.append('')
    row = splitted_data
    table.add_row(row)
html_string = table.get_html_string()
file = open(r"\\192.168.0.100\scanimport\Master\test.html","w")
file.write(html_string)
file.close()
print("done")


