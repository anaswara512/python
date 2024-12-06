w=float(input("enter your weight:"))
h=float(input("enter your height:"))
def bmi(w,h):
    bmi=(w)/(h/100)**2
    return bmi
data=(bmi(w,h))
print("bmi weight is",data)
