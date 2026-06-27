#Random number generation
import random
#print(help(random))
#print(dir(random))
#print(random.randint(1,6,))#For Random Whole int in the given range specially for rolling Dice


#poly Sided Dice
Low = 1
High = 20
#print(random.randint(Low,High))#Range can be also Variables
#To print Random number
#num = random.random()# prints random floating pntnums b/w 0 to 1
#print(num)


'''Program for Rock Paper Scissors game
Options = ("Rock","Paper","Scissors")
Opt ion = random.choice(Options)#eturns Random elelment used majorly for games gives random choice from Options
print(Option)

while True:
    Human = input("Enter your Figure(Rock,Paper,Scissors): ")
    if Human == Option'''


'''#Random Play card order
Cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
Shuffle = random.shuffle(Cards)
print(Cards)'''

#names = ["Yogi", "Smart", "Intelligent", "Dynamic"]#Tuples and Sets are not supported with shuffle
#random.shuffle(names)
#print(names)# Shuffle not support item assignment

'''#Number Guessing Game(Cat And Bull Game)
import random
Lowest_num = 1
Highest_num = 100
Answer = random.randint(Lowest_num,Highest_num)
print(Answer)
Guesses = 0
is_running = True#user guesses num as long program runs and will be False

print("Number Guessing game in python")
print(f"Select number between {Lowest_num} and {Highest_num}")

while is_running:
    Guess = input("Enter your Guess(1 to 100): ")
    if Guess.isdigit():#if enteres numeric digit only
        Guess = int(Guess)
        print(f"you Entered {Guess} which is valid")
        Guesses += 1
        if Guess < Lowest_num or Guess > Highest_num:
            print("That number is out of range")
            print(f"selsct the number b/w {Lowest_num} and {Highest_num}")
        elif Guess < Answer:
            print("You Entered a lower value Try again!")
        elif Guess > Answer:
            print("Your values is higher Try again!")
        else:
            print(f"Correct Answer!,The answer was {Answer}")
            print(f"Number of Guesses: {Guesses}")
    
                  
    else:
        print("Invalid number")
        print(f"Please slesct numer b/w{Lowest_num} and {Highest_num}")
print()'''

'''#Rock,Paper,Scissors
import random
Options = ("Rock","Paper","Scissors")
Running = True
while Running:#to play the game again we use this
    Player = None# Takes the user values
    Computer = random.choice(Options)
    while Player not in Options:
        Player = input("Enter a Option(Rock,Paper,Scissors): ")

    print(f"Player : {Player}")
    print(f"Computer: {Computer}")
    if Player == Computer:
        print("Its been a tie!")
    elif Player == "Rock" and Computer == "Scissors":
        print("You Lose")
    elif Player =="Paper" and Computer == "Rock":
        print("You Won!")
    elif Player == "Scissors" and Computer == "Paper":
        print("You won!")
    else:
        print("You Lost")
    Play_again = input("Play again? (y/n): ").lower()
    if not Play_again == "y":
        Running = False

print("Thanks for Playing")'''
#to get the memory address of any objecct 
list = [1,7,9]
just = id(list)
print(just)


'''#Dice roller program
import random
#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")# for unique code charater for hasky art
#● ┌ ─ ┐ │ └ ┘
"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"
Dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: (" ┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│    ●    │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ●│",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●  ●  ● │",
        "│         │",
        "│ ●  ●  ● │",
        "└─────────┘"),

}
Dice = []#Dice here are nums from 1 to 6
Total = 0
num_of_Dice = int(input("How many dice?: "))
for die in range(num_of_Dice):
    Dice.append(random.randint(1,6))

for die in range(num_of_Dice):
    for line in Dice_art.get(Dice[die]):
        print(line)
print(Dice)
for die in Dice:
    Total += die
print(f"Total: {Total}")'''