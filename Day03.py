# Shopping cart

Item = input("What item do you want?: ")
Quantity = int(input("How many do u want?: "))
Price = float(input("What is the Cost of the item?: "))
Total_Cost = Quantity * Price
print(f"You have bought {Quantity} x {Item}/s")
print(f"You Should pay ${Total_Cost}")
#user i/p validation
Orders = int(input("Enter the no of orders: "))
print(f"You have placed a no of {Orders} orders")


#multiple assignments
Father,Mother,Brother = "Devender","Shirisha","SAi Teja"
Secondary = HigherSecondary = Graduation = "Pass"
print(Secondary)
print(type(Father))
print(Father,Mother,Brother)


# MatLab Game
adjective1 = input("Enter Some Description of something here adjective1: ")
noun1 = input("Enter the noun(name,place,animal,thing) here noun1: ")
verb1 = input("Enter the verb(action word) here verb1: ")
adjective2 = input("Enter Some Description of something here adjective2: ")
noun2 = input("Enter the noun(name,place,animal,thing) here noun2: ")
verb2 = input("Enter the verb(action word) here verb2 that end with "ing": ")
adjective3 = input("Enter Some Description of something here adjective3: ")
noun3 = input("Enter the noun(name,place,animal,thing) here noun3: ")
verb3 = input("Enter the verb(action word) here verb3: ")
print(F"Yesterday i woke up early and helped my father to get some {adjective1}")
print(F"Every Tuesday we go for the {noun1} which is at {noun2} for {verb1} and {verb2}")
print(f"this is only just to {adjective2} our {verb2}")
print(f"My Father {adjective3} me if i refuse {verb3} with him")
a = float(input("Enter the value for a: "))
b = float(input("Enter the value for b: "))
c = float(input("Enter the value for c: "))


#Arithmetc operations
print("Addition:", a + b)
print("Subtraction:", b - c)
print("Multiplication:", a * c)
print("Division:", a / c)
print("Modulus:", a % c)
print("Power:", a ** c)



# Math Functions
x = 12.2
y = 3
z = 9
Result1 = round(x)
print(Result1)
Result2 = abs(y)
print(Result2)
Result3 = pow(z,y)
print(Result3)
Result4 = max(x,y,z)
print(Result4)
Result5 = min(x,y,z)
print(Result5)
Result6 = max(Result1,Result2,Result3,Result4,Result5)
print(Result6)



# Math modules and functions
import math
print(math.pi*2)
print(math.e*3)
print(math.sqrt(25))
print(math.ceil(12.3))#rounds to the upper
print(math.floor(12.9))#Round to the lower



#if statements if statements does something if the cond is T else else is printed
Total_marks = float(input("Enter You marks secured(<=100): "))
if Total_marks >= 80:
    print("You may get into IIT")
elif Total_marks <= 0:
    print("You got negative marks")
elif Total_marks == 0:
    print("You secured 0 marks")
elif Total_marks >= 50:
    print("You can apply for NIT's")
elif Total_marks == 100:
    print("Congrats you secured full")
else:
    print(f"You can't get into IIT's or NIT's with {Total_marks} marks")



# Example2 (Strictly equals)
Your_Result = input("Enter You Result for your UG(Pass/Fail): ")
if Your_Result == "Pass":
    print("Congrats here is your degree to download")
else:
    print("You are not eligible to download the degree")



#Eg2(Bools)
is_Eligible = True
if is_Eligible:
    print("Your ELigible")
else:
    print("Your are not eligible")


#eg3
Name = input("ENter your name: ")
if Name == "":
    print("you have not yet entered your name")
else:
    print (f"Hello {Name}, Welcome to the world of Python")
    Preparing = True
if Preparing:
    print("You are preparing")
else:
    print("You have not yet started your preparation") 


# Simple Calculator
Operator = input("Enter the operator (+, -, *, /, %, **): ")

Num1 = float(input("Enter the first number: "))
Num2 = float(input("Enter the second number: "))

if Operator == "+":
    result = Num1 + Num2
    print(f"{Num1} + {Num2} = {round(result, 2)}")

elif Operator == "-":
    result = Num1 - Num2
    print(f"{Num1} - {Num2} = {round(result, 2)}")

elif Operator == "*":
    result = Num1 * Num2
    print(f"{Num1} * {Num2} = {round(result, 2)}")

elif Operator == "/":
    result = Num1 / Num2
    print(f"{Num1} / {Num2} = {round(result, 2)}")

elif Operator == "%":
    result = Num1 % Num2
    print(f"{Num1} % {Num2} = {round(result, 2)}")

elif Operator == "**":
    result = Num1 ** Num2
    print(f"{Num1} ** {Num2} = {round(result, 2)}")

else:
    print(f"You entered {Operator} an invalid operator")
