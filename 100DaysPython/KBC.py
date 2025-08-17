quesList = ["What is the color of the sky", "What is the first letter of the word 'Red' ", "This is Q3"] 

# ans1 = ["Red", "Blue", "Green", "Yellow"]
# ans2 = [""]

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

    
    


    


