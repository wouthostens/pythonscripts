import jpype
import glob
import os
import csv
import xlrd
from pathlib import Path
import firebase_admin

from firebase_admin import credentials, firestore

jpype.startJVM()

cred = credentials.Certificate(r"\\192.168.0.100\data\DATABASE_DATA\CsvToFirebase\ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)
store = firestore.client()

csv_path = r"\\192.168.0.100\data\DATABASE_DATA\DETAIL"
csv_path_save = r"\\192.168.0.100\data\DATABASE_DATA\DETAIL"
excel_files = glob.glob(r'\\192.168.0.100\data\DELTA\VEDELUX\OFFERTES\*.xlsx')
excel_files.sort(key=os.path.getctime)

for excel in excel_files[-500:]:
    filename = Path(excel).name
    base, ext = os.path.splitext(filename)
    if base.startswith("ORD_"):
        with xlrd.open_workbook(excel) as wb:
            sh = wb.sheet_by_index(0)
            with open(os.path.join(csv_path_save, f"{base}.csv"), 'w', newline='') as f:
                writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                for r in range(sh.nrows):
                    writer.writerow(sh.row_values(r))

jpype.shutdownJVM()

print('Done with excels to csv')


