# Collections:A Single Variable which has multiple values and also Dictionaries
Product_Based = ["Google", "Microsoft","PhonePe","Paypal","Amazon","Flipkart"]. 
#print(Product_Based)
#print(Product_Based[::-1])#[2::-1][::2]
#print(dir(Product_Based))# Displays all the Methods in the collectuions
#print(help(Product_Based))#Gives the description of attributes or methods
#print(len(Product_Based))
#print("Paypal" in Product_Based)#values using the in operator returns bool
#print("Delloitte" in Product_Based)
'''for Company in Product_Based:
    print(Company)'''
'''Product_Based[3] = "Swiggy"# Lists are changable
print(Product_Based)'''
#Product_Based = {"Google", "Microsoft","PhonePe","Paypal","Amazon","Flipkart"}
#Product_Based.append("Delloitte")# adds to end of list
#Product_Based.remove("Flipkart")# removes the elemnet
#Product_Based.insert(5,"FlipKart")
#Product_Based.sort()
#Product_Based.reverse()
#Product_Based.append("Flipkart")
#print(Product_Based.index("Flipkart"))
#print(Product_Based.count("Flipkart"))

#Tuples:are Ordered collections,Unchangable,Indexing is done, Duplicates are allowed, Faster etc
Product_Based = ("Google", "Microsoft","PhonePe","Paypal","Amazon","Flipkart","Flipkart")
#print(Product_Based)
#print(help(Product_Based))
print(dir(Product_Based))
Product_Based.sizeof("Amazon")


#SET:is a collection that is immutable no dupes and not indeex,and no UnOrder only add and remove is possible
#Product_Based = {"Google", "Microsoft","PhonePe","Paypal","Amazon","Flipkart","Flipkart"}
#print(dir(Product_Based))
#print("Microsoft" in Product_Based)
#Product_Based.add("Delloitte")
#print(Product_Based)
#print(len(Product_Based))
#Product_Based.remove("Paypal")
#print(Product_Based)
#print(Product_Based[2])# Return error
#Product_Based.pop()
#print(Product_Based)
#print(Product_Based.count("Flipkart"))#Dupes are not accepted
#Product_Based.clear()
#print(Product_Based)
#for Company in Product_Based:
    #print("Company")
#Tuples:Collections of values that are Ordered and Unchangable,Has Dupes
Product_Based = ("Google", "Microsoft","PhonePe","Paypal","Amazon","Flipkart","Flipkart")
#print(dir(Product_Based))
#print(len(Product_Based))
#print(help(Product_Based))
#print(Product_Based.count("Flipkart"))
#Product_Based.pop()
#Product_Based.add("Delloitte")
#Product_Based.remove("Paypal")
#print(Product_Based)
#print("Paypal" in Product_Based)
#print(Product_Based.index("Paypal"))
#print(Product_Based.count("Flipkart"))
#print(help(Product_Based))
#for Company in Product_Based:
 #   print(Company)

 '''#Shopping Cart Problem
#We use List here bcoz it is Ordered and Changable
Foods = []
Prices = []
Total = 0
while True:
    Food = input("Enter your food item(q to quit): ")
    if Food == "q":
        break
    else:
        Price = float(input(f"Enter the price of the {Food}: $"))
        Foods.append(Food)
        Prices.append(Price)
print("----Your Cart is----")
for Food in Foods:
    print(Food, end = "\t")
for Price in Prices:
    Total += Price
print(f"Your total is {Total}$")'''


'''Books = []
Numbers = []
Total = 0
while Total == 0:
    Book = input("Enter the type of books you have(q to quit): ")
    if Book == "q":
        break
    else:
        Number = float(input(f"Enter the Number of {Book}: $"))
        Books.append(Book)
        Numbers.append(Number)
print("Total books in cart")
for Book in Books:
    print(Book , end = "\v")
for Number in Numbers:
    Total += Number
print(f"Your total is {Total} $")'''

'''# Expense Tracker

Expenses = []
Spent = []
Total = 0
while True:
    Expense = input("Enter your Daily expense(q to quit): ") 
    if Expense.lower() == "q":
        break
    else:
        Spend = float(input(f"Enter your Spendings for {Expense}: $"))
        Expenses.append(Expense)
        Spent.append(Spend)
print("Your Total Expense Spendings")
for Expense in Expenses:
    print(Expense, end = "\v")
for Spend in Spent:
    Total += Spend
    avg = Total // (len(Spent))
    Maximum_Expense = max(Spent)
print(f"The max spennding is {max(Spent)} and is for {max(Expenses)}$")
print(f"The Average spendings is {avg}$")
print(f"Your total amount spent is {Total}$")'''


'''Expenses = []
Spent = []
Total = 0

while Total == 0:
    Expense = input("Enter your daily expense (q to quit): ")

    if Expense.lower() == "q":
        break

    Spend = float(input(f"Enter amount spent on {Expense}: $"))

    Expenses.append(Expense)
    Spent.append(Spend)

print("\n---- Expense Summary ----")

for i in range(len(Expenses)):
    print(f"{Expenses[i]} : ${Spent[i]}")

for amount in Spent:  
    Total += amount

avg = Total / len(Spent)

max_amount = max(Spent)
max_index = Spent.index(max_amount)
print(max_index)
print(max_amount)

print(f"\nHighest Expense: {Expenses[max_index]} = ${max_amount}")
print(f"Average Spending: ${avg:.2f}")
print(f"Total Spending: ${Total:<10}")'''


'''# Cricket Team Scoring
Players = []
Scores =[]
Total = 0
n = int(input("Enter the no of Players you want to enter: "))

for i in range(n):#or 11
    Player = input(f"Enter the {n}Player name: ") 
    Score = int(input(f"Enter the scores of {Player}: "))
    Players.append(Player)
    Scores.append(Score)
print(" Each Players Scores are")
for i in range(len(Players)):
    print(f"{Players[i]}: {Scores[i]}")
for Num in range(len(Scores)):
    Total += Num    
    avg = Total / len(Scores)
max_Num = max(Scores)
max_index = Scores.index(max_Num)
min_Num = min(Scores)
min_index = Scores.index(min_Num)
print(f"High Scored player: {Players[max_index]} made scores =  {max_Num}")
print(f"Low scored Players:{Players[min_index]} made scores = {min_Num}")
print(f"The average is {avg}")
print(f"Total scores made{Total}")'''














