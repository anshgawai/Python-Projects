#take input for number between 5 and 9, raise custom error for everything else
a = input("Enter number between 5 and 9 : ")

#exit program if user enters 'quit', display error for any other string
if a == "quit" : 
    exit()
elif a != "quit" : 
    raise ValueError("Value should be between 5 and 9!")
elif int(a) < 5 or int(a)>9 :
    raise ValueError("Value should be between 5 and 9!")