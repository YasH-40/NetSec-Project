import hashlib

string = input("Enter the string to be Hashed :- ")
salt = "SHAPEAI"                                 #predefined salt

data = hashlib.md5((string+salt).encode())

print("String that added as salt is :-",salt,"\nThe MD5 salted hashed output of given input is :-",data.hexdigest())



string = input("Enter the string to be Hashed :- ")
salt = input("Enter the string to be added as salt :-")          #salt as user input

data = hashlib.md5((string+salt).encode())

print("String that added as salt is :-",salt,"\nThe MD5 salted hashed output of given input is :-",data.hexdigest())