
#Program to check the number of vowels in a word/sentence

#Taking input and initializing the counter variable
a = input("Enter the word/sentence : ")
cV = 0

#checking every character if it is a vowel, if yes, the value of counter variable increases
for i in a : 
    if i == 'a' or i=='A' :
        cV += 1
    elif i== 'e' or i=='E'  :
        cV += 1
    elif i== 'i' or i=='I'  :
        cV += 1
    elif i== 'o' or i=='O'  :
        cV += 1
    elif i== 'u' or i=='U'  :
        cV += 1

if cV > 0  :
    print(a," has ",cV, " Vowel/Vowels" )
else : 
    print("has no vowels")