f = open(r"C:\Users\HINDUJA\OneDrive\Desktop\Python\UNIT 3\File_Handling\text_file\file1.txt","r")#r is used here to avoid slash prm in windows
print('Name of the file is',f.name)
print(f'the file is opened in {f.mode} modde')
str = f.read()
print(str)
f.close()

f = open(r"C:\Users\HINDUJA\OneDrive\Desktop\Python\UNIT 3\File_Handling\text_file\file1.txt",'r')
str1 = f.readline()
print(str1)
f.close()

f = open(r"C:\Users\HINDUJA\OneDrive\Desktop\Python\UNIT 3\File_Handling\text_file\file1.txt",'r')
str2 = f.readlines()
print(str2)
f.close()