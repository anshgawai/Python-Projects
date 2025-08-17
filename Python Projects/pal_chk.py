#Palindrome check program(code doesnt work accurately if there are upper case characters in the middle)

#Taking input
a = input("Enter input to check : ")

# Normalize case (so 'Madam' and 'madam' are treated the same)
a = a.lower()

#list comprehension/creating list on the fly
l1 = [i for i in a]

#checking equality using list slicing, -1 acts as a iterable
if (l1 == l1[::-1]) : 
    print( " is a palindrome")
else: 
    print("is not a palindrome")