import string
import random
n=int(input("Enter the length of Password : \n"))
up=list(string.ascii_uppercase)
low=list(string.ascii_lowercase)
num=list(string.digits)
pun=list(string.punctuation)
allchar=up+low+num+pun
password=[]
for i in range(0,n):
    password.append(random.choice(allchar))
password="".join(password)
print(password)