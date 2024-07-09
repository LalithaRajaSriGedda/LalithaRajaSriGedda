def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def div(n1,n2):
    return n1/n2
def mul(n1,n2):
    return n1*n2
print("please select one operation-\n")
print("1.Add\n")
print("2.Subtraction\n")
print("3.Division\n")
print("4.Multiplication\n")
ch=int(input("select any one option"))
number_1=int(input("enter first number: \n"))
number_2=int(input("enter second number: \n"))
if ch==1:
    print(number_1, "+",number_2,"=",add(number_1,number_2))
elif ch==2:
    print(number_1, "-",number_2,"=",sub(number_1,number_2))
elif ch==3:
    print(number_1, "/",number_2,"=",div(number_1,number_2))
elif ch==4:
    print(number_1, "*",number_2,"=",mul(number_1,number_2))
else:
    print("invalid choice")
    
