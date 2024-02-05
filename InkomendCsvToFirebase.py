import  jpype    
jpype.startJVM() 
import csv
import os
import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate(r"\\192.168.0.100\data\DATABASE_DATA\CsvToFirebase\ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()
csv_path = r"\\192.168.0.100\data\DATABASE_DATA\INKOMEND "
csv_path = csv_path.strip()

for filename in os.listdir(csv_path):
    file_path = os.path.join(csv_path, filename)
    data = []
    headers = ["BLANCO_IMP","KLANTNAAM_IMP","REC.DATUM_IMP","REMBOURS_IMP","BLANCO2_IMP","REF KLANT_IMP","LENGTE_IMP","STEEDS N_IMP","NAAM_IMP","AM/PM/ZAT/AFH_IMP","STRAAT(+ huisnr)_IMP","HUISNR_IMP","LAND_IMP","PC_IMP","GEMEENTE_IMP","COMMENTAAR TRANSPORT_IMP","TELEFOON_IMP","EMAIL_IMP","CONTACTPERSOON_IMP","GSM-NR_IMP","ma v1_IMP","ma t1_IMP","ma v2_IMP","ma t2_IMP","di v1_IMP","di t1_IMP","di v2_IMP","di t2_IMP","wo v1_IMP","wo t1_IMP","wo v2_IMP","wo t2_IMP","do v1_IMP","do t1_IMP","do v2_IMP","do t2_IMP","vr v1_IMP","vr t1_IM","vr v2_IMP","vr t2_IMP","za v1_IMP","za t1_IMP","za v2_IMP","za t2_IMP","aantal (1)_IMP","oms.(COLLI)_IMP","Kg (10000)_IMP","Vol(50)_IMP","aantal (1)3_IMP","oms.(COLLI)4_IMP","Kg (10000)5_IMP","Vol(50)6_IMP","aantal (1)7_IMP","oms.(COLLI)8_IMP","Kg (10000)9_IMP","Vol(50)10_IMP","aantal (1)11_IMP","oms.(COLLI)12_IMP","Kg (10000)13_IMP","Vol(50)14_IMP","aantal (1)15_IMP","oms.(COLLI)16_IMP","Kg (10000)17_IMP","Vol(50)18_IMP","aantal (1)19_IMP","oms.(COLLI)20_IMP","Kg (10000)21_IMP","Vol(50)22_IMP","SCANCODE_IMP","SCANCODE23_IMP","SCANCODE24_IMP","SCANCODE25_IMP","SCANCODE26_IMP","SCANCODE27_IMP","DISTRIBUTION CENTER_IMP","INVOICE CODE_IMP","WERFLEVERING_IMP","HANDTEKENING VERPLICHT_IMP","LEVERINGSDATUM2_IMP","NEUTRALE LEVERING2_IMP","BLANCO","KLANTNAAM","REC.DATUM","REMBOURS","BLANCO2","REF KLANT","LENGTE","STEEDS N","NAAM","AM/PM/ZAT/AFH","STRAAT(+ huisnr)","HUISNR","LAND","PC","GEMEENTE","COMMENTAAR","TELEFOON","EMAIL","CONTACTPERSOON","GSM-NR","ma v1","ma t1","ma v2","ma t2","di v1","di t1","di v2","di t2","wo v1","wo t1","wo v2","wo t2","do v1","do t1","do v2","do t2","vr v1","vr t1","vr v2","vr t2","za v1","za t1","za v2","za t2","aantal (1)","oms.(COLLI)","Kg (10000)","Vol(50)","aantal (1)2","oms.(COLLI)3","Kg (10000)4","Vol(50)5","aantal (1)6","oms.(COLLI)7","Kg (10000)8","Vol(50)9","aantal (1)10","oms.(COLLI)11","Kg (10000)12","Vol(50)13","aantal (1)14","oms.(COLLI)15","Kg (10000)16","Vol(50)17","aantal (1)18","oms.(COLLI)19","Kg (10000)20","Vol(50)21","SCANCODE","SCANCODE22","SCANCODE23","SCANCODE24","SCANCODE25","SCANCODE26","DISTRIBUTION CENTER","INVOICE CODE","WERFLEVERING","HANDTEKENING VERPLICHT","LEVERINGSDATUM","NEUTRALE LEVERING","ORDER","KLANT","REF","L","LEVERING","OPMERKINGEN ORDER&KLANT","TOEVOEGEN","EXTRA","ORDER #","Leverdatum Jordy","Type","Naam2","Naam (vervolg	of tav)","Straat","Huisnummer","Postcode","Plaats","Land3","Telefoon4","Email adres","Afleverinstructie","Rembours5","Eenheid","Gewicht","Lengte6","Breedte","Hoogte","Omschrijving","Barcode"]
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
                obj.popitem()
                data.append(obj)
                line_count += 1
    print(filename)
    print(f'Processed {line_count} lines.')
    filename = str(filename.strip().split('.')[0])
    for dat in data:
        if list(dat.values())[1] == "LATTESTORE":
            doc_ref = store.collection(u'inkomend').document("otYcfJNM54EU3MPTvpzo").collection("lattestore").document(filename).set({"name": filename})
            doc_ref = store.collection(u'inkomend').document("otYcfJNM54EU3MPTvpzo").collection("lattestore").document(filename).collection("producten").document(dat.get("SCANCODE")).set(dat)
        if list(dat.values())[1] == "VEDELUX":
            doc_ref = store.collection(u'inkomend').document("otYcfJNM54EU3MPTvpzo").collection("vedelux").document(filename).set({"name": filename})
            doc_ref = store.collection(u'inkomend').document("otYcfJNM54EU3MPTvpzo").collection("vedelux").document(filename).collection("producten").document(dat.get("SCANCODE")).set(dat)
    os.remove(file_path)
print('Done')