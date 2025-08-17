""" Welcome to the Student Helper App!
Choose an option:
1. Manage Shopping List
2. Enter Subject Marks
3. View Today's Canteen Menu
4. Play the Quiz
5. Understand Tuple vs List
6. Exit  """

def playQuiz(a, b) : 
    quesList = ["What is the color of the sky", "What is the first letter of the word 'Red' ", "This is Q3"] 

    ansList = ["Blue", "R", "3"]
    amtList = [1000, 2000, 5000]

    i = int(0)
    while (i < len(quesList)):
         print(quesList[i])
         userAns = input("Enter your answer : ")

         if userAns == ansList[i] :
            i = i+1
            continue
         else:
            print("You have lost the game!")
            print("You have won amount : ", amtList[i])
            break      
         
