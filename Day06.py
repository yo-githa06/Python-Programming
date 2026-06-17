#For loop executes for a specific no of time

# For Loops
for x in range(1,11,2):
    print(x)

for x in (reversed(range(1, 11,4))):
    print(x)


Phn_No= "9390582865"
for x in Phn_No:
    print(x) 

for x in range(0,6):
       if x == 3:
        continue# continue keyword is used to skip the iteration when x is 3
       print(x)

for x in range(6,13):
    if x == 8:
        continue
    else:
        print(x)#this is for-else the else block prints 12 because it is the no after the loop ends and the loop is not terminated by break but by the condition of the loop becomes false

for x in range (0,9):
    if x == 3:
        break
    else:
        print(x)

for Y in range(0,39):
    if Y == 13:
        continue#break
    else:
        print(Y)#the keyword is common in both while loops and the for loops ie., continue which skips over an iteration
else:
    print(x)

    
for Y in range(0,39):
    if Y == 13:
        break
    else:
        print(Y)# the keyword Break is used to break or stops the iteration


for i in range(9,19):
    if i == 15:
        continue
    print(i)

#Eg1CountDown Timer
import time#time module
Timing = int(input("Enter Your time in seconds: "))# set the time for sleep
#use any loop
for x in range(Timing,0,-1):#for x in range(0,Timing):(or)#for x in reversed(range(0,Timing)):
    time.sleep(1)#wait for entered Timing no of Secs 
    # Calculating the secs
    Seconds = x % 60
    Minutes = int(x / 60) % 60# in this case theere are 60 secs in min and  will not exceed 60, so use mod
    Hours = int(x / 3600) % 24 #there are 3,600 secs in an hr
    Days = int(x / 86400)
    print(f"{Days:02}:{Hours:02}:{Minutes:02}:{Seconds:02}")
time.sleep(5)# every iteration takes aroud5 second in the loop

print("Hello Lazy")

#While Loop
import time
Time_Left = int(input("Enter the time in seconds: "))
while Time_Left > 0:
    time.sleep(1)
    Time_Left -= 1
    Seconds = Time_Left % 60
    Mins = int(Time_Left / 60 ) % 60
    Hrs = int(Time_Left / 3600) % 24
    Days = int(Time_Left / 86400)
    print(f"{Days:02}:{Hrs:02}:{Mins:02}:{Seconds:02}")
print("Hello Lazy")

#Method2
while True:
    time.sleep(1)
    Time_Left -= 1
    Seconds = Time_Left % 60
    Mins = int(Time_Left / 60 ) % 60
    Hrs = int(Time_Left / 3600) % 24
    Days = int(Time_Left / 86400)
    print(f"{Days:02}:{Hrs:02}:{Mins:02}:{Seconds:02}")
    if Time_Left <= 0:
        Time_Left = int(input("Enter the time in seconds: "))

#eg3
while True:
    time.sleep(1)
    Time_Left -= 1
    Seconds = Time_Left % 60
    Mins = int(Time_Left / 60 ) % 60
    Hrs = int(Time_Left / 3600) % 24
    Days = int(Time_Left / 86400)
    print(f"{Days:02}:{Hrs:02}:{Mins:02}:{Seconds:02}")
    if Time_Left <= 0:
        break


import time

seconds = int(input("Enter seconds: "))

while seconds:
    mins, sec = divmod(seconds, 60)
    hrs, mins = divmod(mins, 60)
    days, hrs = divmod(hrs, 24)

    print(f"{days:02}:{hrs:02}:{mins:02}:{sec:02}")

    time.sleep(1)
    seconds -= 1

print("Countdown Finished!")

#For Loop Egs
#Eg1:Sum of N numbers
Num = int(input("Enter a Num: "))
Total = 0
for i in range(1,Num + 1):
    Total += i
    print(f"Sum = {Total}")

#Sum of 10 numbers
Total = 0
for i in range(1,11):
    Total += i
    print(f"Sum = {Total}")


#Factorial of numbers
Number = int (input("Enter a number: "))
fact = 1
for i in range(1,Number+1):
    fact *= i
    print("Factorial =", fact)

#Multiplication Table
number = float(input("Enter a number: "))
for i in range(1,11):
    print(f"{i} X {number} = {i*number}")

#Odd numbers from 1 to 20
for i in range(1,21,2):
    print(f"The odd nums from 1 to 20 are:{i}")

# print numbers from 100 to 1
for i in reversed(range(1,101)):
    if i == 50:
        break
    else:
        print(i)

for i in range(100,0,-1):
    if i % 2 != 0:
        print(i, "is a odd number")
    else:
        print(i, "is a even number")

for i in range(50,0,-1):
     if i <= 50 and i%2 == 0:
        print(i,"is a even small number")
     else:
         print(i,"is a odd small number")

#Calculate the Compound Interest
Principle = float(input("Enter your Principle amount here: "))
Rate = float(input("Enter Your rate of int: "))
Time = int(input("ENter the time Period: "))
for i in range(0,1):
    Compound_Interest = Principle * pow((1+Rate/100),Time)
    print(f"The Compound Interest is for principle = {Principle}, Rate = {Rate} and Time is {Time} years ,\n The coumpound interest id calculated as {Compound_Interest} ")
