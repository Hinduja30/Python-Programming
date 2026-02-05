import csv

data = [
    ['Name' , 'age' , 'City'],
    ['Abbot',25,'NewYork'],
    ['Bob',30,'LosAngeles'],
    ['Chang',35,'Chicago'],
]

with open('output.csv','w+',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    writer.writerow(['Alice',25,'NewYork'])
with open('output.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

