from simplegmail import Gmail
import csv
import firebase_admin
from firebase_admin import credentials, firestore
import os

cred = credentials.Certificate("./ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()


def batch_data(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

gmail = Gmail()

messages = gmail.get_unread_inbox()
for message in messages:
    message.mark_as_read()
    if message.attachments:
        for attm in message.attachments:
            file_path = r"C:\Users\wouth\OneDrive - Hogeschool VIVES\Bureaublad\vdm\EmailToFirebase\ "
            file_path = file_path.strip()
            filename=""
            print('File: ' + attm.filename)
            filename =  attm.filename
            attm.save() 
            file_path = file_path + filename
            data = []
            headers = []
            with open(file_path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=';')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        for header in row:
                            headers.append(header)
                        line_count += 1
                    else:
                        obj = {}
                        for idx, item in enumerate(row):
                            if item !=",,,,,":
                                obj[headers[idx]] = str(item)
                        obj.popitem()
                        data.append(obj)
                        line_count += 1
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