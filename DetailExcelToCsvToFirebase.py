import  jpype    
import glob
from pathlib import Path    
jpype.startJVM() 
from asposecells.api import Workbook
import xlrd
import csv
import os
import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate(r"\\192.168.0.100\data\DATABASE_DATA\CsvToFirebase\ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()

excel_files = glob.glob(r'\\192.168.0.100\data\DELTA\VEDELUX\OFFERTES\*.xlsx')
csv_path = r"\\192.168.0.100\data\DATABASE_DATA\DETAIL "
csv_path_save = r"\\192.168.0.100\data\DATABASE_DATA\DETAIL\ "
csv_path = csv_path.strip()
csv_path_save = csv_path_save.strip()
excel_files.sort(key=os.path.getctime)

for excel in excel_files[-500:]:
    fileName = Path(excel).name
    fileName = fileName.split('.')[0]+'.csv'
    if(fileName.startswith("ORD_")):
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

data = []
for filename in os.listdir(csv_path):
    file_path = os.path.join(csv_path, filename)
    csv_bestand = []
    split_values = []
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            values_of_row = ""
            for i in row:
                values_of_row = values_of_row + i +" "
            csv_bestand.append(values_of_row)
            if "OMSCHRIJVING" in values_of_row or "DESCRIPTION" in values_of_row:
                split_values.append(line_count)
            line_count +=1
        start = 0
        split_values.append(line_count)
        omschrijving = ""
        for j in csv_bestand[:split_values[0]]:
            omschrijving = omschrijving + j +" \n "
        ref = filename.split("ref")[1].translate({ord('_'): " "}).lstrip()
        store.collection(u'detail').document("SJxHpofDGRv0wnppOdd6").collection("vedelux").document(filename).set({'ref': ref.replace('.csv', ""),'Omschrijving': omschrijving})    
        obj = {}
        for i in split_values:
            einde = i 
            if start ==0:
                obj = {}
                for l in csv_bestand[int(start)+4:einde]: 
                    split_value = l.split(':')
                    if len(split_value)==1:
                        if split_value[0] == "         ":
                            if obj.get(' Référence') is not None: 
                                ref = obj.get(' Référence').replace('/', '  ')
                                store.collection(u'detail').document("SJxHpofDGRv0wnppOdd6").collection("vedelux").document(filename).collection('controles').document(ref).set(obj)    
                            elif obj.get(' Referentie'):
                                ref = obj.get(' Referentie').replace('/', '  ')
                                store.collection(u'detail').document("SJxHpofDGRv0wnppOdd6").collection("vedelux").document(filename).collection('controles').document(ref).set(obj)    
                            elif obj.get(' Hoogte') is not None or obj.get(' Art. ') is not None or obj.get(' Hauteur') is not None or obj.get(' Motor') is not None or obj.get(' Moteur') is not None or obj.get('kooflijst') is not None:
                                ref = str(start)
                                store.collection(u'detail').document("SJxHpofDGRv0wnppOdd6").collection("vedelux").document(filename).collection('controles').document(ref).set(obj)    
                            obj = {}
                        else:
                            val = split_value[0].split('    ')
                            if not val[0] == "":
                                if(val[0].__contains__("Kooflijst")):
                                    obj["kooflijst"] = split_value[0]
                                else:
                                    obj[str(val[0])] = str(val[1])
                            val = ""
                    else:
                        obj[str(split_value[0])] = str(split_value[1])  
            elif start !=0:
                obj = {}
                for l in csv_bestand[int(start)+3:einde]: 
                    split_value = l.split(':')
                    if len(split_value)==1:
                        if split_value[0] == "         ":
                            if obj.get(' Référence') is not None: 
                                ref = obj.get(' Référence').replace('/', '  ')
                                store.collection(u'detail').document("SJxHpofDGRv0wnppOdd6").collection("vedelux").document(filename).collection('controles').document(ref).set(obj)    
                            elif obj.get(' Referentie'):
                                ref = obj.get(' Referentie').replace('/', '  ')
                                store.collection(u'detail').document("SJxHpofDGRv0wnppOdd6").collection("vedelux").document(filename).collection('controles').document(ref).set(obj)    
                            elif obj.get(' Hoogte') is not None or obj.get(' Art. ') is not None or obj.get(' Hauteur') is not None or obj.get(' Motor') is not None or obj.get(' Moteur') is not None or obj.get('kooflijst') is not None:
                                ref = str(start)
                                store.collection(u'detail').document("SJxHpofDGRv0wnppOdd6").collection("vedelux").document(filename).collection('controles').document(ref).set(obj)    
                            obj = {}
                        else:
                            val = split_value[0].split('    ')
                            if not val[0] == "":
                                if(val[0].__contains__("Kooflijst")):
                                    obj["kooflijst"] = split_value[0]
                                else:
                                    obj[str(val[0])] = str(val[1])
                            val = ""
                    else:
                        obj[str(split_value[0])] = str(split_value[1])
            start = i
    os.remove(file_path)
print('done adding to firebase')