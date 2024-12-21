import os

#f = open("instruction.txt","x")

'''f = open("instruction.txt","a+")
data = f.read()
print(data)
print(type(data))

print("using readLine instruction")
dataline = f.readline()
print(dataline)
print("for printing only few characters")
strings = f.read(45) # read only first 45 characters
print(strings)
f.write("\nthanks")
data = f.read()
print(data)
f.close()'''

#using with Syntax
with open("main.py","r+") as f:
    data = f.read()
    print(data)
os.remove("cwithdsa.dev")