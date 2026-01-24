import os
import csv

base = os.path.dirname(__file__)
path = os.path.join(base,"data.csv")
with open(path,'r') as file:
    reader = csv.reader(file , skipinitialspace=True)
    for row in reader:
        print(row)
    file.seek(0)
    print()
    print("dictionary representation")
    reader1 = csv.DictReader(file)
    for dict in reader1:
        print(dict)
    