# This is a program to compare three numbers

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

#checking equality individualy
if(a>b and a>c):
    print("first number is the largest")
elif(b>a and b>c) : 
    print("second number is the largest")
else : 
    print("third number is the largest")

#comparing equality of three numbers
if (a==b and b==c and a==c ) : 
    print("All numbers are equal")

#checking equality of two numbers and comparing it to the third
elif(a==b):
    if(a>c) : 
        print("first two numbers are equal and largest")
    else : 
        print("third number is the largest")
elif(b==c) :
    if(b>a) : 
        print("last two numbers are equal and largest")
    else : 
        print("first number is the largest")
elif(a==c) :
    if(a>c) : 
        print("first and last numbers are equal and largest")
    else : 
        print("second number is the largest")