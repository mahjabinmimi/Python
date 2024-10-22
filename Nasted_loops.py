#WAP to  check if a number entered by the user is odd or even.
number = int(input("enter any integer:"))
reminder= number%2
if(reminder == 0 ):
    print("even")
else:
    print("ODD")
    
#WAP to find the greatest of 3 numbers entered by the user.
num1 = input("enter number:")
num2 = input("enter number:")
num3 = input("enter number:")
if(num1>num2):
    if(num1>num3):
        print("num1 is the greatest")
elif(num1<num2):
    if(num2>num3):
        print("num2 is the greatest")
else:
    print("num3 is the grestest")

#WAP to check if number is a multiple of 7 or not.
a = int(input("enter any integer:"))
if(a%7 == 0):
    print(a," a is a multiple of 7")
else:
    print(a," is not a multiple of 7")


