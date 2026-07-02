#By default, a function must be called with the correct number of arguments.

#However, sometimes you may not know how many arguments that will be passed into your function.

#*args and **kwargs allow functions to accept a unknown number of arguments. with and without keywords respectively


'''def Banks(*Accounts):
    return(f"Your account is now {Accounts[2]} and getting to {Accounts[3]}")
print(Banks("Saving","Empty","Current","Salary"))
#If you do not know how many arguments will be passed into your function, add a * before the parameter name.

#This way, the function will receive a tuple of arguments and can access the items accordingly: withount the keywords
def emotions(*args):
    return(f"the mood swings can be varied to {args[0]},{args[2]},{args[1]},{args[3]}")
print("Happy","Sad","Sorrow","Cry","Hurt","Insult")'''

'''# using the regular parameterswith *args but they shld preceed
def regular(name,*age):
   for i in age:
       print(name,age)
regular("Good Morning","yo!","19")'''

'''def Wish(greeting ,*Name):
    for i in Name:
        print(greeting,i)
Wish("Hi","Yogi","Yogitha","Yo!Yo!")

# Sum of Numbers 
def Sum(*Num):
    Total = 0
    for num in Num:
        Total += num
    return Total
print(Sum(1,8,6,0,3))
print(Sum(34,98,77,55))'''

# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
#This way, the function will receive a dictionary of arguments and can access the items accordingly:
'''def Career(**Company):
    Running = True
    while True:
        choice = int(input("Enter a number between (0,1): "))

        if choice == 0:
            print(f"Sai Teja may continue in {Company['MNC']}")
        elif choice == 1:
            print(f"Sai Teja may get into {Company['StartUps']}")
        else:
            print("Please enter only 0 or 1")

        cont = input("Enter to continue (y/n): ").lower()

        if cont == "n":
            Running = False

Career(MNC="Concentrix", StartUps="Sridevi")'''

'''# eg2
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "yogi", age = "19", city = "hyderbad")'''

#

'''def Example(**kwargs):
    print("Type: ",type(kwargs))
    print("Name: ", kwargs["Name"])
    print("Age: ",kwargs["Age"])
    print("ID: ",kwargs["Roll"])
    print("Year: ",kwargs["Years"])

Example(Name = "D. Yogitha", Age = 19, Roll = 39,Years = "2nd")


def Address(**kwargs):
    for key,value in kwargs.items():#for key in kwargs.keys():# for valu in kwargs.values
        print(f"{key} : {value} ")

print(Address(Country = "India",
              State = "Telangana",
              City = "Hyd"))'''


'''#Regular argument, args, and arbitary keyword arguments
def last_ex(Greeting,*args,**kwargs):
    print("hello",Greeting)
    print("To all ", args)
    print("Schools,Qualifiaction",kwargs.values())#kwargs.keys()#kwargs.values


print(last_ex("Welcome","Yogitha","Shirisha",School = "HFHS", Qualification = "Btech"))'''