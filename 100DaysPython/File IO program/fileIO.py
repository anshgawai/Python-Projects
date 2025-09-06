#Program for File handling operations

f = open('myfile.txt' , 'w')

# text = f.read()        #used to extract contents from 'myfile.txt'
# print(text)
# f.close()              #closing the file

text = f.write("Hello world!\n")


f1 = open('myfile.txt' , 'a')
txt2 = f.write("This is Ansh!")     

"""used to append text to a file, 
openning in write mode will overwrite the text in the 
file while using append will add text to the file """

f1.close()

with open('myfile.txt' , 'r') as f:         #there is no need to close a file by using with statement
    txt = f.readline()         # readline() method reads only single lines from the file
    print(txt)


f = open('myfile.txt' , 'r')

while True : 
    line = f.readline()
    if not line : 
        break
    print(line)

with open('myfiles1.txt' , 'w') as f:
    lines = ["line1\n", "line2\n", "line3\n"]
    f.writelines(lines)

with open('myfiles2.txt' , 'w') as f:
    lines = ["Hi", "This is", "Ansh!"]
    f.writelines(lines)