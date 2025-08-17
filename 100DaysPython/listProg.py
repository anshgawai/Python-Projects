'''
          **Exercise 7:**
        Take 5 numbers as input and store them in a list. Then:

        * Print the max number
        * Sort the list
        * Remove duplicates
'''

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))
num4 = int(input("Enter the fourth number : "))
num5 = int(input("Enter the fifth number : "))


numList = [num1, num2, num3, num4, num5]

print("The greatest number in the list is : ", max(numList))

numList.sort() 
print ( "The sorted list is : " , numList)

remDupl = set(numList)
print("The list after removing the duplicates : ", remDupl)

