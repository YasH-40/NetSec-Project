import hashlib

string = input("Enter the string to be Hashed :- ")

data = hashlib.md5(string.encode())

print("The MD5 hashed output of given input is :-",data.hexdigest())
