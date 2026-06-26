#2D Collections: This is a collections of collection
#2D Lists: which is list of lists
#Eg1
Fruits = ["Bananas", "Apples","Oranges","Mangoes"]
Veggies = ["Potato","Tomato","Carrot"]
Meat = ["Chicken","Mutton","Fish"]
#Foods = [Fruits,Veggies,Meat]
#Fruits[2] = "Grapes"
#print(Fruits)
#print(Foods)
#print(Foods[2])# This returns all the list at index 2 ie., with rows
#print(Foods[2][1])# this returns the elment at indexed as rows and colns 
Foods = [["Bananas", "Apples","Oranges","Mangoes"],["Potato","Tomato","Carrot"],["Chicken","Mutton","Fish"]]#List made of lists
#Foods = [Fruits,Veggies,Meat]
#Foods = [{"Bananas", "Apples","Oranges","Mangoes"},{"Potato","Tomato","Carrot"},{"Chicken","Mutton","Fish"}]List made of sets is possible 
#Foods = {{"Bananas", "Apples","Oranges","Mangoes"},{"Potato","Tomato","Carrot"},{"Chicken","Mutton","Fish"}}set made of sets is not possible
#Foods = {("Bananas", "Apples","Oranges","Mangoes"),("Potato","Tomato","Carrot"),("Chicken","Mutton","Fish")}#set made of Tuples not possible
#Foods = ({"Bananas", "Apples","Oranges","Mangoes"},{"Potato","Tomato","Carrot"},{"Chicken","Mutton","Fish"})#Tuple of sets possible
#Foods = (["Bananas", "Apples","Oranges","Mangoes"],["Potato","Tomato","Carrot"],["Chicken","Mutton","Fish"])#Tuple of Lists possible
#Foods = {("Bananas", "Apples","Oranges","Mangoes"),("Potato","Tomato","Carrot"),("Chicken","Mutton","Fish")}#set of Tuples possible
#Foods = {("Bananas", "Apples","Oranges","Mangoes"),("Potato","Tomato","Carrot"),("Chicken","Mutton","Fish")}#set made of tuples not possible
#Foods = {["Bananas", "Apples","Oranges","Mangoes"],["Potato","Tomato","Carrot"],["Chicken","Mutton","Fish"]}#Set  made of Lists not possible
#Foods = [("Bananas", "Apples","Oranges","Mangoes"),("Potato","Tomato","Carrot"),("Chicken","Mutton","Fish")]#List of Tuples possible
for i in Foods:#This loop iterates over rows
    for coln in i:#This loop iterates overscolumns 
        print(i)#Prints The len no of times each row

for i in Foods:#This loop iterates over rows
    #for coln in i:#This loop iterates overscolumns 
        print(i)#prints all the lements of 1d
        print()# Goes to nxt line after every Iterations

#Num_Pad 
Numerals = [[1,2,3],
            [4,5,6],
            [7,8,9],
            ["*",0,"#"]]
for i in Numerals:
        for Colns in i:
                print(Colns, end = "\t")
        print()

#Num_Pad 
Numerals = ((1,2,3),
            (4,5,6),
            (7,8,9),
            ("*",0,"#"))
for i in Numerals:
        for Colns in i:
                print(Colns, end = "\t")
        print()

#Num_Pad 
Numerals = {(1,2,3),
            (4,5,6),
            (7,8,9),
            ("*",0,"#")}
for i in Numerals:
        #for Colns in i:
                #print(Colns, end = "\t")
        print()


#quiz game
Questions =("Are you eligible to be a Btech Graduate?: ","Are you eligible to rule and argue with parents?: ","Are your really giving your 100%?: ","Till When are you Going to complete your Basics in sql,Python,DsA,Software Engineering?: ","What are u Planning to start from 50 days from now?: ")
Options = (("A. Yes(if i really put my efforts for 1 year from now)","B. No(If i won't Work hard)","C. Yes(All because i am clearing all sem's)","D. No(If i am lazy)"),
           ("A. No","B.OffCourse ","C.Definetely ","D. IDk"),
           ("A. No(Still trying)","B. i dont have to ","C.Yes i am  ","D.IDK "),
           ("A. 10thJan ","B. 10thDec","C. 10thFeb","D. 10thJuly "),
           ("A. Python dev and DSA","B. Dance,Acting","C. GovtExam Prep","D. Chilling"))

Answers = ("A", "A", "A", "D", "C")
Guesses =[]# since required to be appended
Score = 0
Question_num = 0

for Question in Questions:
    print("-------You realize---------")
    print(Question)
    for Option in Options[Question_num]:
        print(Option)#print(Options,end ="\t")prints for 4 times
    print()
    Guess = input("Guess your answer: ").upper()
    Guesses.append(Guess)
    if Guess == Answers[Question_num]: #if Guesses list is = to answers at index of Question no
        Score += 1
        print("Correctly Answered")
    else:
        print("Incorrect Answers")
        print(f"{Answers[Question_num]} is correct answer")
    Question_num += 1


print("------Results are-------")

print("Answers: ",end = "")
for Answer in Answers:
    print(Answer,end = " ")
print()
print("Guesses: ", end = " ")
for Guess in Guesses:
    print(Guess, end = " ")
    print()
Score = int(Score / len(Questions) * 100)
print(f"Total Score is {Score}%")

#QUiz Game
Questions = ("Who is the father of the nation?: ","Who is the current PM of India?: ","Who is the Pm of USA?: ", "Is India a Federal Nation and follows Soverignity?: ","Which is the popular Big Four company in India?: ")

Options = (("A. Dr.Br.Ambedkar","B. APJ Abdul Kalam","C. Donald Trumph","D. Mahatma gandhi"),
           ("A. Indra Gandhi","B. Narendra Modi","C. Pandit jawaharlal Nehru","D. Nirmala Sitaraman"),
           ("A. Narendra Modi","B. Williams","C. Donald Trumph","D. Obamma"),
           ("A. Yes","B. No","C. Not decided","D. Still processing"),
           ("A. MicroSoft", "B. Google","C. Deloitte","D. Amazon"))

Answers = ("D","B","C","A","C")
Guesses = []# Since i need to append
Score = 0
Question_num = 0
for Question in Questions:
    print("-----Here are your Questions------")
    print(Question)
    for Option in Options[Question_num]:
        print(Option,end = " ")
    print()
    Guess = input("Enter Your Answer(A,B,C,D): ").upper()
    Guesses.append(Guess)
    if Guess == Answers[Question_num]:
        Score += 1
        print("Correctly Answered!")
        print("Your Answer is Correct!")
    else: 
        print("Sorry,Your Answer is incorrect!")
        print(f"The correct Answers are{Answers[Question_num]}")
    Question_num += 1

print("---Results---")
print("Answers are: ",end = " ")
for Answer in Answers:
    print(Answer, end = " ")
print()

print("Guesses: " ,end = " ")
for Guess in Guesses:
    print(Guess, end = " ")
print()


Score = int(Score  / len(Questions)) * 100
print(f"Your total Score is {Score}")
#Dictionaries

States_capitals = {"Telangana": "Warangal",
                   "Karnataka": "Bengaluru",
                   "Odisha":"Locknow",
                   "Delhi":"Agra"}
#print(dir(States_capitals))#Gives various attributes and methods
#print(help(States_capitals))#Gives descrition
print(States_capitals.get("Telangana"))#returnsthe values for the key 
print(States_capitals.get("Jaipur"))# prints none if not found in dict
if States_capitals.get("Jaipur"):
    print("Thst capital exists")
else:
    print("That capital is not existing in dict")
States_capitals.update({"Jammu & kashmir" : "Ladhak" })#This update method can add or update to the dictionary
States_capitals.update({"AndhraPradesh":"Amaravathi"})
States_capitals.update({"Telangana": "Hyderabad"})
#States_capitals.pop("Odisha",)# to remove akey values pair
#States_capitals.popitem()#popitem() method removes the latest key valur pair from dict

#print(States_capitals.keys())#returns all the keys of the dict
Keys = States_capitals.keys()
print(Keys)

for Key in States_capitals.keys():
    print(Key)

print(States_capitals)


# To get all the values from a dictionary use values() method
#print(States_capitals.values())
Values = States_capitals.values()
for Value in States_capitals.values():
    print(Value)

#to get both the key and value use .items() method 
print(States_capitals.items())#returs a 2D list of dict items
#Item = States_capitals.items()
for item in States_capitals.items():
    print(item)
for Key, Value in States_capitals.items():
    print(f"{Key}:{Value}")
#Example to keep track of menu using Dictionary
#Mimicing Concession Stand Program
Menu = {"PopCorn": 190,
        "Pizza": 299,
        "Burger": 169,
        "Franky": 199,
        "Chizza": 300,
        "Coke": 170,
        "Puffs": 49
        }

Cart = []# to keep track of user cart orselcted items
Total = 0

print("--------Here is your Menu-------")
for Key,Value in Menu.items():
    print(f"{Key:20}: ${Value:.3f}")
print()

while True:
    Food = input("Enter items to cart(q to quit): ").lower()
    if Food == "q":
        break
    elif Menu.get(Food) is not None:
        Cart.append(Food)
        
for Food in Cart:
    Total += Menu.get(Food)
    print(Food,end = " ")

print()
print(f"Total is ${Total:.2f}")