#here we convert text file into csv file
import csv
import os

base = os.path.dirname(__file__)
path = os.path.join(base , 'emp_details.txt')

with open(path , 'r') as file:
  reader = csv.reader(file , delimiter=";")
  line_count = 0
  for row in reader:
    if line_count == 0:
      print(f"column names are: {",".join(row)}")
      line_count += 1
    else:
      print(f"{row[0]} has id {row[1]} and works in {row[2]} department and earns{row[3]}.")
      line_count += 1
  print(f"processed {line_count} lines")
  print()
  file.seek(0)
  reader1 = csv.DictReader(file , delimiter=";",skipinitialspace=True)
  line_count = 0
  for row in reader1: # no if here because first line is already taken in dictreader
      print(row)
      print(f"{row['Name']} has id {row['Empid']} and works in {row['Dept']} department and earns {row['Salary']}.")
      line_count += 1
  print(f"processed {line_count} lines")

    

