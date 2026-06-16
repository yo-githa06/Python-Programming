#variables And Datatypes
'''name = "Yogitha"
age = 19
Weight = 56.5
print(name)
print(age)
print(Weight)
'''


# This is also a comment since no multi line comment is supported in python
'''FirstName = "Yogitha"
Age = 19
Adress = "HYd"
Email = "yoogitha57@gmail.com"
print(F"The selected participant is {FirstName} and of {Age} old and she is from {Adress} and refer her email id {Email}")# this is the tech of using f string 
Qualified_age = 18
Qualified_age -= 1
is_selected = True
Weight = 89.9


if Qualified_age >= 18:
    print("You are eligible to vote")
else:
    print("You are not suppose to vote") 

    
if is_selected:
    print("Congrats you are selected")
else:
    print("Sorry, You rae rejected")# always for bool the true prints the if block and False prints the else block


if Weight <= 90.0:
        print("You are healthy")
else:
        print("You are Unhealthy")'''



# Various Conversions in TypeCasting
'''name = "Doodimadugula Yogitha"
Curent_Age = 19
Salary = 100000.45
is_Working = True


#int to str
Curent_Age = str(Curent_Age)
print(Curent_Age)
#Curent_Age += "1"
#print(Curent_Age)


# float to int
Salary = int(Salary)
Salary += 10000
print(Salary)


#int to float
Curent_Age = float(Curent_Age)
print(Curent_Age)


#bool to str
is_Working = str(is_Working)
print(is_Working)
print(type(is_Working))


# str to bool
name = bool(name)#prints False if the variable of str is empty only withe the Quotes
print(name)


# intto bool
Curent_Age= bool(Curent_Age)
print(Curent_Age)


# float to boool
Salary = bool(Salary)
print(Salary)'''


#Eg Programs
#UserInput Function
"""print(input("Enter your college name: "))
Name = input("Enter you name: ")
print(f"Hello Dear {Name}, How can i help you?")
Return_AS_Str = int(input("Enter your age: "))
Return_AS_Str +=1 
print(Return_AS_Str)
print(type(Return_AS_Str))"""# user input fun always returns str in that case type casting is used



#1 add of 3 nos
'''a = float(input("Enter a's value: "))
b = float(input("Enter b's value: "))
c = float(input("Enter c's value: "))
print(3*a+4*b+3*c)



# Area of Square
side = float(input("Enter the side of the square: "))
print(f"This perimeter is {4*side}cm²")
print(f"The Area of the square is {side**2}cm²")