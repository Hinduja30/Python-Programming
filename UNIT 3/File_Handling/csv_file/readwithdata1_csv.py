import os
import csv

base = os.path.dirname(__file__)
path = os.path.join(base, 'data1.csv')

with open(path , 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
    file.seek(0)
    print()
    readers = csv.reader(file , delimiter=";")
    for row in readers:
        print(row)
    print()
    file.seek(0)
    reader1 = csv.DictReader(file , delimiter=";")
    for row in reader1:
        print(row)