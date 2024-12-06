a=float(input("enter a number:"))
b=float(input("enter a number:"))
def calculator(a,b):
        print("1.addition\n2.subtraction\n3.multiplication\n4.division\n5.invalid choice")
        for i in range(6):
            c=int(input("enter your choice:"))
            if(c==1):
                print("sum=",a+b)
            elif(c==2):
                print("sub=",a-b)
            elif(c==3):
                print("mul=",a*b)
            elif(c==4):
                if(b!=-0):
                    print("div=",a/b)
                else:
                    print("division is not possible")
            elif(c==5):
                exit()
            else:
                print("invalid operation")  
calculator(a,b)