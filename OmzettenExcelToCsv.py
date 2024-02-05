"""
voor gebruik heb je de nodige libaries nodig. 
importeer deze door volgende commando's uit te voeren.

installeren van python, pip zoek online
python get-pip.py

pip install pandas
pip install pathlib
pip install glob 
 """
import  jpype     
import glob
import pandas as pd
from pathlib import Path    
jpype.startJVM() 
from asposecells.api import Workbook
import xlrd
import csv
import datetime

excel_files = glob.glob(r'\\192.168.0.100\data\DELTA\VEDELUX\OFFERTES\*.xlsx')
csv_path = r'\\192.168.0.100\scanimport\Detail\VEDELUX\ '
csv_path = csv_path.rstrip(csv_path[-1])
for excel in excel_files:
    fileName = Path(excel).name
    fileName = fileName.split('.')[0]+'.csv'
    if(fileName.startswith("ORD_"+str(datetime.date.today().year))):
        workbook = Workbook()
        workbook.save(csv_path + fileName)
        with xlrd.open_workbook(excel) as wb:
            sh = wb.sheet_by_index(0)  
            with open(csv_path+fileName, 'w', newline='') as f:   
                c = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                for r in range(sh.nrows):
                    c.writerow(sh.row_values(r))
jpype.shutdownJVM()
