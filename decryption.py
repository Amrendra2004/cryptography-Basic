import os
import string

char = string.ascii_letters + string.digits + string.punctuation + " "
char=list(char)

#given key
f=open("key.txt","r")
key=f.read()
key=list(key)

#cipher Text
message=input("Enter your cipher Text:-")

#Decryption
str=""
for i in message:
    letter = key.index(i)
    str += char[letter]

print("message:-",str)


