import hashlib

string = input("Enter the string to be Hashed :- ")

md5 = hashlib.md5(string.encode())
sha1 = hashlib.sha1(string.encode())
sha256 = hashlib.sha256(string.encode())
blake2b = hashlib.blake2b(string.encode())

print("The MD5 hashed output of given input is :-",md5.hexdigest())
print("The SHA1 hashed output of given input is :-",sha1.hexdigest())
print("The SHA256 hashed output of given input is :-",sha256.hexdigest())
print("The Blake2b hashed output of given input is :-",blake2b.hexdigest())