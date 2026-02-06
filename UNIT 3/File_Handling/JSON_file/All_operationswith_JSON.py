import json
import os

base = os.path.dirname(__file__)
path = os.path.join(base ,"name.json")
path1 = os.path.join(base ,"emp.json")
path2 = os.path.join(base ,"name.txt")
path3 = os.path.join(base, "output.json")

person='{"name":"Bob","languages":["English","French"]}'
person_dict = json.loads(person)
print(person_dict)
print(person_dict['languages'])
print()

#read a file parse into dictionary that is load
with open(path,"r") as file:
    data = json.load(file)
    print(data) 
print()

with open(path1,"r",encoding='utf-8') as file:
    jsondata = json.load(file)
print("type of json object:",type(jsondata))
print()

for name in jsondata:
    print("Name:",name)
    print("phone number:",jsondata[name]["number"])
    print("Age:",jsondata[name]["age"])
    print("adress:")
    for line in jsondata[name]["address"]:
        print(line)
print()

#convert dict into json that is use dump 
name_dict = {'name':'Lupin','age':33,'children':None}
name_json = json.dumps(name_dict)  
print(name_json) 
print()
#write JSON to afile
name_dict = {"name":"Andromeda","languages":["English","French"],"married":True ,"age":32}
with open(path2,'w') as json_file:
    json.dump(name_dict, json_file)
print()

person_string='{"name":"Dennis","languages":"English","numbers":[2, 1.6, null]}'
person_dict=json.loads(person_string)
print(json.dumps(person_dict, indent = 4, sort_keys=True))

with open(path1,"r") as file:
    jsonData = json.load(file)
    result =[]
    for name in jsondata:
        data =[name,len(jsonData[name]["address"])]
        result.append(data)
    print("person vs number of address lines")
    for name, lines in result:
        print(name + " ",end=" ")
        print(lines)

with open(path1,"r") as file:
    fileData = file.read()
    jsondata = json.loads(fileData)
    phonerecord = {}
    for name in jsonData:
        phonerecord[name] = jsonData[name]["number"]
    with open(path3,"w+") as outfile:
        json.dump(phonerecord,outfile)
    print("Process Complete!")

  