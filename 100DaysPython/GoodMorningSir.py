import time

timeStamp = time.strftime('%H:%M:%S')
print(timeStamp)
hr = int(time.strftime("%H"))
min = int(time.strftime("%M"))
sec = int(time.strftime("%S"))


if(hr<12 and hr==0 and min>=0 and sec>=0):
    print("Good Morning sir!")
elif(hr>=12 and hr<16 and min>=0 and sec>=0):
    print("Good Afternoon sir!")
elif(hr>=16 and hr<20  and min>=00 and sec>=0):
    print("Good Evening sir!")
elif(hr>=20 and min>=00 and sec>=0):
    print("Good Night sir!")
else:
    print("Invalid time")
