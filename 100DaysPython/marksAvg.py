'''
    Create a dictionary to store marks for 3 subjects. Then:

    * Print all subjects with marks
    * Find the average

'''
sciMarks = int(input("Enter Science Marks : "))
mathsMarks = int(input("Enter Maths Marks : "))
histMarks = int(input("Enter History Marks : "))

subjMarks = {
    "Science marks" : sciMarks,
    "Maths marks"   : mathsMarks,
    "History marks" : histMarks
}

print(subjMarks)
avgMarks = (subjMarks["Science marks"] + subjMarks["Maths marks"] + subjMarks["History marks"])/3
print("The average of all subjects is : ", avgMarks)
