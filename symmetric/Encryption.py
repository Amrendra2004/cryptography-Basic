import random
import string
import os

char = string.ascii_letters + string.digits + string.punctuation + " "
char = list(char)

#symmictric key
key=list.copy(char)
random.shuffle(key)
a=open("key.txt","w")
key1=""
for i in key:
    key1 +=i
a.write(key1)

#Encryption
plainText=input("Enter your message:-")
cipherText=""
for i in plainText:
    letter=char.index(i)
    cipherText+=key[letter]

print("ciphertext:-",cipherText)
