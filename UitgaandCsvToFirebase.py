import  jpype    
jpype.startJVM() 
import csv
import os
import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate(r"\\192.168.0.100\data\DATABASE_DATA\CsvToFirebase\ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()
csv_path = r"\\192.168.0.100\data\DATABASE_DATA\UITGAAND "
csv_path = csv_path.strip()

for filename in os.listdir(csv_path):
    file_path = os.path.join(csv_path, filename)
    data = []

    headers = ["BLANCO","KLANTNAAM","REC.DATUM","REMBOURS","BLANCO2","REF KLANT","LENGTE","STEEDS N","NAME","AM/PM/ZAT/AFH","STRAAT(+ huisnr)","HUISNR","COUNTRY","PC","GEMEENTE","COMMENTAAR","TELEFOON","E-MAIL","CONTACTPERSOON","GSM-NR","ma v1","ma t1","ma v2","ma t2","di v1","di t1","di v2","di t2","wo v1","wo t1","wo v2","wo t2","do v1","do t1","do v2","do t2","vr v1","vr t1","vr v2","vr t2","za v1","za t1","za v2","za t2","aantal (1)","oms.(COLLI)","Kg (10000)","Vol(50)","aantal (1)2","oms.(COLLI)3","Kg (10000)4","Vol(50)5","aantal (1)6","oms.(COLLI)7","Kg (10000)8","Vol(50)9","aantal (1)10","oms.(COLLI)11","Kg (10000)12","Vol(50)13","aantal (1)14","oms.(COLLI)15","Kg (10000)16","Vol(50)17","aantal (1)18","oms.(COLLI)19","Kg (10000)20","Vol(50)21","SCANCODE","SCANCODE22","SCANCODE23","SCANCODE24","SCANCODE25","SCANCODE26","DISTRIBUTION CENTER","INVOICE CODE","WERFLEVERING","HANDTEKENING VERPLICHT","LEVERINGSDATUM","NEUTRALE LEVERING"]
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
                obj = {}
                for idx, item in enumerate(row):
                    if item !=",,,,,":
                        obj[headers[idx]] = str(item)
                    if item !="":
                        obj[headers[idx]] = str(item)
                data.append(obj)
                line_count += 1
    print(filename)
    print(f'Processed {line_count} lines.')
    filename = str(filename.strip().split('.')[0])
    for dat in data:
        """if list(dat.values())[1] == "LATTESTORE":"""
        doc_ref = store.collection(u'uitgaand').document("otYcfJNM54EU3MPTvpzo").collection("ontime").document("BdzUXKZyexSXX6M7jXfz").collection("new").document(filename).set({"name": filename})
        doc_ref = store.collection(u'uitgaand').document("otYcfJNM54EU3MPTvpzo").collection("ontime").document("BdzUXKZyexSXX6M7jXfz").collection("new").document(filename).collection("producten").document(dat.get("SCANCODE")).set(dat)
        """if list(dat.values())[1] == "VEDELUX":
            doc_ref = store.collection(u'uitgaand').document("otYcfJNM54EU3MPTvpzo").collection("vedelux").document(filename).set({"name": filename})
            doc_ref = store.collection(u'uitgaand').document("otYcfJNM54EU3MPTvpzo").collection("vedelux").document(filename).collection("producten").document(dat.get("SCANCODE")).set(dat)
"""
    os.remove(file_path)
print('Done')