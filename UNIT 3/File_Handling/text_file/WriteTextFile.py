with open('file2.txt','w') as file:
    content_number = file.write("hello world!")#returns number of characters return
    print(f"the content written is : {content_number}")

lines=["First line\n","Second line\n","Third Line\n"]
with open('file3.txt','w') as file:
    file.writelines(lines)
file = open('file3.txt','r')
s = file.read()

print(s)
file.seek(0)
s1 = file.read()
print(s1)#prints ntg as points to EOF if no seek()

status = file.closed
print(f"whether the file is closed? {status}")

file.close()
print("whether the file is closed? ",file.closed)

