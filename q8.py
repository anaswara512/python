def calculator():
    for i in range(6):
        a=float(input("enter a number:"))
        b=float(input("enter a number:"))
        print("1.addition\n2.subtraction\n3.multiplication\n4.division\n5.invalid choice")
        c=int(input("enter your choice:"))
        if(c==1):
            sum=a+b
            return sum
        elif(c==2):
            sub=a-b
            return sub
        elif(c==3):
            mul=a*b
            return mul
        elif(c==4):
            if(b!=-0):
                div=a/b
                return div
            else:
                print("division is not possible")
        elif(c==5):
            exit()
        else:
            print("invalid operation")
for i in range(6):            
    data=calculator()
    print(data)