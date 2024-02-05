import  jpype    
import glob
from pathlib import Path    
jpype.startJVM() 
from asposecells.api import Workbook
import xlrd
import csv
import os
import datetime
import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate(r"\\192.168.0.100\data\DATABASE_DATA\CsvToFirebase\ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()

excel = r'C:\Users\wouth\OneDrive - Hogeschool VIVES\Bureaublad\vdm\CsvToFirebase\SALES_DATA.xlsx'

file_path = r"C:\Users\wouth\OneDrive - Hogeschool VIVES\Bureaublad\vdm\CsvToFirebase\SALES_DATA.csv"
csv_path = r"C:\Users\wouth\OneDrive - Hogeschool VIVES\Bureaublad\vdm\CsvToFirebase\ "
csv_path_save = r"C:\Users\wouth\OneDrive - Hogeschool VIVES\Bureaublad\vdm\CsvToFirebase\ "
csv_path = csv_path.strip()
csv_path_save = csv_path_save.strip()

fileName = 'SALES_DATA.csv'
workbook = Workbook()  
workbook.save(csv_path_save + fileName)
with xlrd.open_workbook(excel) as wb:
    sh = wb.sheet_by_index(0)  
    with open(csv_path_save+fileName, 'w', newline='') as f:   
        c = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        for r in range(sh.nrows):
            c.writerow(sh.row_values(r))  
jpype.shutdownJVM()

print('Done with excels to csv')


def batch_data(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

data = []
headers = []
with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            for header in row:
                headers.append(header.lower())
            line_count += 1
        else:
            obj = {}
            for idx, item in enumerate(row):
                obj[headers[idx]] = str(item)
            data.append(obj)
            line_count += 1
    print(f'Processed {line_count} lines.')
for dat in data:
    if (list(dat.values())[2] != ""):
        dat.update({'datum': datetime.datetime.utcfromtimestamp((int(float((list(dat.values())[2]))) - 25569) * 86400.0).strftime("%m/%d/%Y")})  
    if(list(dat.values())[9]!=""):
        dat.update({'vervaldat': datetime.datetime.utcfromtimestamp((int(float((list(dat.values())[9]))) - 25569) * 86400.0).strftime("%m/%d/%Y")})  
    if(list(dat.values())[15]!=""):
        dat.update({'factuurdat': datetime.datetime.utcfromtimestamp((int(float((list(dat.values())[15]))) - 25569) * 86400.0).strftime("%m/%d/%Y")})  
    if(list(dat.values())[20]!=""):
        dat.update({'bev_dat': datetime.datetime.utcfromtimestamp((int(float((list(dat.values())[20]))) - 25569) * 86400.0).strftime("%m/%d/%Y")})  
    doc_ref = store.collection(u'sales').document(list(dat.values())[1]).set(dat)
print('Done')