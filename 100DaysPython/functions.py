""" Write a program defining 4 functions:
    1. Addition
    2. Subtraction.
    3. Greater than
    4. pass the Lesser than function

    Take input from the user, and display all the 3 functions """

def addNum(a, b):
    Add= a+b
    # print("The addition is : ", Add)
    return Add

def subNum(a, b):
    Sub= a-b
    print("The subtraction is : ", Sub)

def isGreaterThan(a, b):
    if(a > b):
        print("The first number is greater")
    else:
        print("The second number is greater")

def isLessThan(a, b):
    pass


# c = int(input("Enter the first number : "))
# d = int(input("Enter the second number : "))

# addNum(c, d)
# subNum(c, d)
# isGreaterThan(c, d)