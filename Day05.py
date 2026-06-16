
 # if in case we will wait for the users to enter the name we use while loop
# while loop executes some  code WHILE some condition remains true or until it is becomes false
while Name == "":
    print("You did not enter Your name")
    Name = input("ENter your name: ")# if while cond is true the executes the states under the while and the others Potentially forever untill the while is no longer false(And this is just done to escape out of the While loop otherwise we will be continuasly in while or to avoid the Infinite loops)

print(f"Hello {Name} Welcome to the Loops session in python")


# Example for Infinite loop
while Name == "":
    print("You did not enter ur name")

print(f" Hello {Name} Welcome to Pyhton")# This is an infinite loop it executes while is False


AGE = int(input("Enter Your age: "))


while AGE <= 0:
    print("Age can't be -ve")
    AGE = int(input("Enter your age: "))# this avoids the infinite loops or to escape
print(f"Your age is {AGE}")


result = input("Enter your result(Pass/Fail): ")
while result == "Pass":
    print("Congratulations on passing the exams")
    Marks = int(input("Enter your marks: "))# Here the loop continuous because the while is still True t avoid this or escape the loop we need to first make while false to come out of it
print(f"Wow Congrats once again for securing {Marks}")


while result == "Fail":
    print("I am So Sorry to here you that you were unable to clear the exam,Why don't you apply for recounting")
    result = input("Enter your result after recount (Pass/Fail)")
print(f"Wow Congrats once again for securing for ur {result} result in exams after recount")


Python_Course = input("Enter your FeedBack here(Like/Dislike): ")
while Python_Course == "Dislike":
    print(" I am so Sorry that you were unhappy with this course in python,Why don't you switch to online courses available plenty of such on online")
    Python_Course = input("Enter your Feedback on learning Python after exploring the online platforms(Like/Dislike): ")
print(f"Oh that so great You are enjoying and so privileged to know that you {Python_Course} after refering to the online platforms")

food = input("Enter a fav food u frequently order(q to quit): ").lower()
while food == "q":
    print(f"Why did u press {food}")
    food = input("Enter any other food item you order: ")
print(f"That means you order {food} frequently")


Disired_Dress = input("Enter if u found the dress u searched in app(Yes/No): ").lower()
while Disired_Dress == "no":
    print("Oh Dress not found, just reseach again")
    Disired_Dress = input(f"Enter if u found the dress u researched in app(Yes/No): ")
print(f"Oh you got ur dress Finally! {Disired_Dress}")


SSC_Marks = float(input("Enter the points in b/w (1 -10): "))
while SSC_Marks < 1 or SSC_Marks > 10:
    print(f"Your marks are inavlid {SSC_Marks} Try again")
    SSC_Marks = int(input("Enter Your points again: "))
print(f"You Got {SSC_Marks} points in SSC")


FeedBack = int(input("Enter your feedback b/w (1-5): "))
while FeedBack < 1 or FeedBack > 5:
    print("You entred incorrect feedback try again")
    FeedBack = int(input("Re-Enter your feedback here: "))
print(f"Thank you for rating {FeedBack} for us")


Gsoc_Age = int(input("Enter your age: "))
Gsoc_Gender.lower() = input("Enter your Gender(Male/Female): ")
while Gsoc_Age <= 18 and Gsoc_Gender != "female":
    print("Sorry, You are not eligible for Google Girls Summer of codes Try again with valid inputs")
    Gsoc_Age = int(input("Re-enter your Age: "))
    Gsoc_Gender = input("Re-enter your Gender: ")
print("Congrats, On your Success Register on google girls summer of codes")

# Compound Interest
Principle = 0
Rate = 0
Time = 0

while Principle <= 0:
    Principle = float(input("Enter the Principle amount: "))
    if Principle <= 0:
        print("Principle can't be less than or equal to zero")

while Rate <= 0:
    Rate = float(input("ENter the Rate of Interest: "))
    if Rate <= 0:
        print("Rate can't be less than ir equal to zero")
while Time <= 0:
    Time = int(input("Enter the amount of time in years: "))
    if Time <= 0:
        print("Time can'tt be leass than or equals to zero")
print(Principle)
print(Rate)
print(Time)
Total = Principle * pow((1 + Rate / 100),Time)
print(f"The total Compound interest is or the balance after {Time} years is {Total:,.2f} in $")
      
#Compound Interest that takes 0
Principle = 0
Rate = 0
Time = 0

while Principle < 0:
    Principle = float(input("Enter the Principle amount: "))
    if Principle < 0:
        ("Principle amount can't be negativ or less than 0")

while Rate < 0:
    Rate = float(input("Enter the Rate of interest: "))
    if Rate < 0:
        print("Rate of interest can't be less than 0")

while Time < 0:# In These egs the while loop never enters due to condition is false for that use True in while loop which always enters to the while loops
    Time = int(input("ENter the time in years: "))
    if Time < 0:
        print("The time can't be leass than 0")
print(Principle)
print(Rate)
print(Time)
Total = Principle * pow((1 + Rate / 100), Time)
print(f"The total balance after {Time} is {Total} in $")

#Compound interes with bools values
Principle = 0
Rate = 0
Time = 0

while True:
    Principle = float(input("Enter the Principle amount: "))
    if Principle <= 0:
        print("Principle amount can't be negative or less than 0")
    else:
        break

while True:
    Rate = float(input("Enter the Rate of interest: "))
    if Rate <= 0:
        print("Rate of interest can't be less than 0")
    else:
        break

while True:# In These egs the while loop never enters due to condition is false for that use True in while loop which always enters to the while loops
    Time = int(input("ENter the time in years: "))
    if Time <= 0:
        print("The time can't be less than 0")
    else:
        break
print(Principle)
print(Rate)
print(Time)
Total = round(Principle * pow((1 + Rate / 100), Time), 4)
print(f"The total balance after {Time} is {Total} in $")

#eg for social media networkings
LinkedIn_Connections = int(input("Enter No of LinkedIn_Connections: "))
Youtube_Subscribers = int(input("Enter No of Youtube_Subscribers: "))
GitHub_Followers = int(input("Enter No of GitHub_Followers: "))
while LinkedIn_Connections <= 0:
    LinkedIn_Connections = int(input("Enter your total LinkedIn connections: "))
    if LinkedIn_Connections <= 0:
        print("Your LinkedIn Connections can't be zero")
    else :
        break
while Youtube_Subscribers <= 0:
    Youtube_Subscribers = int(input("Enter your total Youtube subscribers: "))
    if Youtube_Subscribers <= 0:
        print("Your Youtube Subscribers can't be zero")
    else :
        break
while GitHub_Followers <= 0:
    GitHub_Followers = int(input("Enter your total GitHub_Followers: "))
    if GitHub_Followers <= 0:
        print("Your Youtube GitHub_Followers can't be zero")
    else :
        break
print(f"Yours total LinkedIn networks is {LinkedIn_Connections:.3f}, Youtube networks is {Youtube_Subscribers:>10}, and GitHube networks is {GitHub_Followers:^10}")




                          
















    



