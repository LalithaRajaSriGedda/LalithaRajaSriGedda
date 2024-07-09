import string
import random
length=int(input("enter password length:"))
print("choose character to set the password:")
print("1.Digits\n")
print("2.Letters\n")
print("3.Special characters\n")
print("4.Exit\n")
characterlist=""
while(True):
    ch=int(input("Pick a number"))
    if ch==1:
        characterlist +=string.ascii_letters
    elif ch==2:
        characterlist +=string.digits
    elif ch==3:
        characterlist +=string.punctuations
    elif ch==4:
        break
    else:
        print("please consider a correct option")
password=[]
for i in range(length):
    randomchar=random.choice(characterlist)
    password.append(randomchar)
print("The random password is"+ "".join(password))
    
