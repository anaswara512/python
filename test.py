a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter a number"))
if(c==1):
    print("sum=",a+b)
elif(c==2):
    print("sub=",a-b)
elif(c==3):
    print("mul=",a*b)
elif(c==4):
    if(b!=0     ):
        print("div=",a/b)
    else:
        print("division is not possible with zero")
elif(c==5):
        exit()
else:
    print("invalid operation")
