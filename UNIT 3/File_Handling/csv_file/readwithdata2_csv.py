import os
import csv
base = os.path.dirname(__file__)
path = os.path.join(base ,"data2.csv")

with open(path , "r") as file:
    fieldnames =["Name","Age","Profession"]
    reader = csv.DictReader(file , delimiter=";",fieldnames=fieldnames)
    for row in reader:
        print(row)

    