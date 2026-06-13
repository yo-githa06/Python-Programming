# Weight converter Program
Weight = float(input("Enter your Weight: "))
Unit = input("Specify the units in kilograms or Pounds(Kg or Lb): ").lower() 
if Unit == "kg":
    Weight = Weight * 2.205
    unit = "Lbs"
    print(f"Your Weight is {round(Weight, 2)} in the unit of {unit} ie., Pounds")
elif Unit == "Lb":
    Weight = Weight / 2.205
    unit = "Kgs"
    print(f"Your Weight is {round(Weight, 2)} in the unit of {unit} ie., Kilograms")
else:
    print(f"You entered an invalid unit {Unit}")


# Temperature Converter
Unit = input("Enter the Temperature's unit ie., in celsius or fahrenheit (C or F): ")
Temperature = float(input("Enter the temperature: "))
if Unit == "C":
    Temperature = (Temperature * 9/5) + 32
    unit = "F"
    print(f"The Temperature is {round(Temperature, 2)} in the unit of {unit} ie., Fahrenheit")
elif Unit == "F":
    Temperature = (Temperture - 32) * 5/9
    unit = "C"
    print(f"The Temperature is {round(Temperature,2)} in the unit of {unit} ie., Celsius")
else:
    print(f"You have entered an invalid Unit {Unit}")


#Logical Operators evaluates multiple condition(OR,And,Not)
Temp = 24
is_Sunny = False
if Temp >= 30 and is_Sunny:
    print("It is Stormy out there")
    print("It is Sunny")
elif Temp <= 20 and is_Sunny:
    print("It is cool out there")
    print("It is Sunny")
elif Temp <= 0 and not is_Sunny: 
    print("It is Snowy Out there")
    print("It is a Windy or stormy Day")
elif Temp >= 30 or is_Sunny:
    print("It is Stormy out there")
    print("It is Sunny")
elif Temp <= 20 or is_Sunny:
    print("It is cool out there")
    print("It is Sunny")
elif Temp <= 0 or not is_Sunny: 
    print("It is Snowy Out there")
    print("It is a Windy or stormy Day")


Marks = 50
Result = "Promoted"
if Marks >= 85 and Result == "pass":
    print(f"Congrats you have passed the examand you Marks are{Marks}")
elif Marks <=50 and Marks != 35  and Marks > 35 and Result == "Promoted":
    print(f"You are promoted and you Marks are{Marks}")
elif Marks <= 35 or Result == "Fail":
    print(f"Sorry, You are failed and you Marks are {Marks}")
else:
    print("You have invalid marks")

Ans = False
Num = 12
if Num  >= 50 or not Ans:# not Gives the False for bools
    print("You have Wrong Ans")
else:
    print("You ans right")

#Conditional Expressions (if else)
Num = 5
print("Multiple of 5" if Num %5 == 0 else "Non Diveisible by 5" )

Num = 4
print("Multiple of 2" if Num % 2 == 0 else "Non Diveisible by 2")

Num = float(input("Enter any number: "))
Result = f"{Num} isMultiple of 3" if Num %3  == 0 else "Non Diveisible by 3"
print(Result)

Number = float(input("Enter any number: "))
Result = f"{Number}Even" if Number % 2 == 0 else "Odd"
print(Result)

Result = -2
Ans = "you have +ve" if Result >= 0 else "-ve"
print(f"{Result} is {Ans}")
a = 10
b = 20 

print(f"Max_val is a = {a}" if a>b else f"Max_val is b = {b}")
print(f"Min_val is a = {a}" if a<b else f"Min_val is b = {b}")

AGE = int(input("Enter Your age: "))
Result3 = (f"Your are {AGE} Adult" if AGE >= 18 else f"You are {AGE} minor")
print(Result3)

Temp = float(input("Enter Today's Temp: "))
print(f"Today is a humid day {Temp}°C" if  Temp >= 25 else f"Today is so cold {Temp}°C")
Password = input("Enter Your Password: ")
Access = "Yogitha Is given access" if Password == "Yogitha@06" else "Invalid Credentials"
print(Access)


#String Methods
Name = input("Enter Your Name: ")
Mo_no = input("Enter ur contact: ")
House_No = input("Enter You House number: ")
print(len(Name))
print(Name.find("Y"))
print(Name.rfind(" "))#ives last recurence in the name of a specific's chars index position
print(Name.capitalize())#makes only the first Char in str Capital and remaining small
print(Name.lower())
print(Name.upper())
print(Name.isdigit())#Returns T/F only if the string contains digits or not chars
print(Mo_no.isalpha())#Returns T/F only if the str holds chars or Alphabets not nay spacesor any no's
print(Mo_no.isdigit())
print(Mo_no.count("9"))#Counts and returns the number of specific chrs in the Str
print(House_No.count("-"))
print(Mo_no.replace("9","6"))


#String Indexing
Balanced_Diet = "Milk","Fruits","Dry Fruits","Water","Juices","Rice","Veggies","Green leaves","Salad","Curd","Chapathi","Vermicelli"
Name = "Doodimadugula Yogitha"
print(f"I Love to have only {Balanced_Diet[2]}")
print(Balanced_Diet[2 : 4])    # End index is exclusive while start is inclusive
print(Balanced_Diet[0 : 12])
print(Name[2 : 4])
print(Name[0 : 21])# This prints all the values or chars in the str
print(Name[5 :])
print(Balanced_Diet[3:])#prints all till end of str
print(Name[-1])# indexing in reverse
print(Name[-13])
print(Name[-21])#returns Exactly in seq because in reverse the index does'nt start from 0
print(Name[:3])# prints from the start
print(Name[::4])# prints the steps frpm start to the count
print(Balanced_Diet[3:13:2])
print(Balanced_Diet[:12:3])
print(Name[0:22:2])
print(Name[1::3])
Last_Name = Name[-7::]
print(f"The last name is {Last_Name}")
Diet = Balanced_Diet[-11::]
print(f"I diet i had was {Diet}")
Last_Name = Name[-7::2]
print(f"The last name is {Last_Name}")
Diet = Balanced_Diet[-2::]
print(f"I diet i had was {Diet}")
Reverse = Name[::-1]
print(Reverse)
#Reverse = Balanced_Diet[::-2]
Reverse = Balanced_Diet[-3::-2]
Reverse = Balanced_Diet[-2:-11:-2]
print(f"The reverse is {Reverse}")
Phone_No = "9390582865"
result = Phone_No[-4::]
print(f"The last 4 digits is {result}")
print(Phone_No[::-1])
print(Phone_No[:-10:-2])
print(Phone_No[::2])


# Format Specifiers: Used in the placeholders While using the f strings beside the values nd to get the desired format
Profit1 = -1200.345
Profit2 = 78000.9065
Profit3 = 4450.6754

print(f"Profit 1 is %{Profit1:.2f}")
print(f"Profit 2 is %{Profit2:.8f}")
print(f"Profit 3 is %{Profit3:.1f}")#.2f or 1f will round of the value to 2 position or 1 respectively where f -means floating Point number
print(f"Profit 1 is %{Profit1:010}")# Preceed a value with 0 and Give the space before the value
print(f"Profit 2 is %{Profit2:012}")
print(f"Profit 3 is %{Profit3:04}")
print(f"Profit 1 is %{Profit1:<10}")
print(f"Profit 2 is %{Profit2:<10}")
print(f"Profit 3 is %{Profit3:<10}")# these are left Justified
print(f"Profit 1 is%{Profit1:>10}")# tHSE IS ARE RIGHT JUSTIFIED
print(f"Profit2 is %{Profit2:>10}")
print(f"Profit3 is%{Profit3:>10}")
print(f"Profit3 is%{Profit1:+10}")
print(f"Profit1 is%{Profit2:+10}")
print(f"Profit2 is%{Profit3:+10}")
print(f"Profit1 is % {Profit1:+}")
print(f"Profit2 is % {Profit2: }")# this space Gives blank space for +ve No's
print(f"Profit1 is % {Profit1: }")
print(f"Profit1 is % {Profit1:+,.2f}")# , is a separator of the digits
print(f"Profit2 is % {Profit2:+,.2f}")
print(f"Profit3 is % {Profit3:+,.2f}")
Name = input("Enter you name: ")
if Name == "":
    print("Please enter your name")
    #Name = input("Enter Your name: ")This does'nt work in If else
else:
    print(f"Hello {Name}")
