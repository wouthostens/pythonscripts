import csv
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r"\\192.168.0.100\data\DATABASE_DATA\CsvToFirebase\ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()

file_path = r"\\192.168.0.100\scanimport\Master\Stock.csv"

def batch_data(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

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

for dat in data:
    if len(dat) >11:
        dat.pop('')
    doc_ref = store.collection(u'master').document("XvPREReAOoTp3DBe3rTV").collection("stock").document(list(dat.values())[0]).set(dat)
print('Done')