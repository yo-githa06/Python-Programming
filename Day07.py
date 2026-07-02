#Reverse of a Number
Numeral = input("Enter a number: ")
Reverse = ""
for i in Numeral:
    Reverse = i + Reverse
    #print(f"The reverse of {Numeral} is {Reverse}")
    print("Revers:",Reverse)


# Reverse of a number using While loop
Numerator = int(input("Enter a number: "))
Reverse = ""
while Numerator >= 0:
    Numerator 
    Reverse = i + Reverse
    print()

#while Loop egs
i = 1
while i <= 10:
    print(i)
    i += 1
#CountDown
i = 10
while i > 0:
    print(i)
    i -= 1 

#Finding the sum until the user enters Zero
Total = 0
while Total == 0:
    Numer = int(input("Enter a number: "))
    if Numer == 0:
        break

    Total += Numer
    print("The sum is ", Total)
num = input("Enter a number: ")

reverse = 0

for digit in num:
    reverse = digit + reverse

print("Reverse:", reverse)
#reverse of a number using arithemetic nums
'num = int(input("Enter a nummber: "))
reverse = 0
digit = len(str(num))
for i in range(digit):
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reverse:", reverse)

num = int(input("Enter a nummber: "))
reverse = 0
while num > 0:

    digit = digit  % 10
    reverse = digit + 10 * reverse
    num = num // 10
print("Reverse:", reverse)


#For loop using the number range for that need to convert to the strng first 
num_count= input("Enter a number")
digit_count = len(num_count)
num = int(num_count)
Reverse = 0
for i in digit_count:# this iterates till the len of the number (no of times)
    digit = num % 10# Gets the last digit (remainder)
    Reverse = Reverse * 10 + digit# Appends the digit to the reverse number
    num = num // 10#now the umber becomes reduces and the remaining num cntinues to iterate# Floor division removes the last digit
print(f"The reverse of the number is: {Reverse}")

# Test code
num = int(input("Enter a number: "))
reverse = ""
for i in range(len(str(num))):
    digit = num % 10
    reverse = reverse + str(digit)
    num = num//10
print("Reverse:", reverse)
# Simple FOr loop Example without ranf=ge Function Directly wuith the Stringa s i/p
num = input("Enter a number: ")
reverse = ""
for i in num:
    reverse = i + reverse
print("Reverse:" , reverse)

num = int(input("Enter a number: "))
reverse = ""
for i in range(str(num)):
    reverse = i + str(reverse)
print("reverse:", reverse)

#Using While loop for numbers
num = int(input("enetr a no: "))
Reverse = 0
while num > 0:
    digit = num % 10
    Reverse = digit + 10 * Reverse
    num = num // 10
    print("Reverse:", Reverse)
print(f"Reverse: {Reverse:.2f}")
#Using While loop for strings
num = input("ENtera  number: ")
reverse = ""
i = 0
while i< len(num):
    reverse = num[i] +reverse
    i += 1
print("Reverse:", reverse)
#eg2
Numeral = input("Enter a string: ")

Reverse = ""
i = 0

while True:
    if i == len(Numeral):
        break

    Reverse = Numeral[i] + Reverse
    print("Reverse:", Reverse)
    i += 1
Numeral = input("Enter a string: ")

Reverse = ""
i = 0

while True:
    if i >= len(Numeral):
        break

    Reverse = Numeral[i] + Reverse
    i += 1

print("Reverse:", Reverse)

# String Slicing
num = input("ENter a  number: ")
reverse = num[::-1]
print("Reverse:", reverse)


for x in range(3):# this loop iterateds for 3 times
    for i in range(1,50,2):# Here it is the  (Statrt,end,Step)
    #print(i,end=" ")
    #print(i,end = "\n")# normally prints in next line always
     print(i, end = "")#gisves results side by not in nxt line
    print()# This blank Print state inside the Outer loop  will result eah iteration in new line


#Rows = int(input("Enter the no of rows: "))
#Cols = int(input("ENter the no og columns: "))
#Symbol = input("Enter a Symbol: ")
# this is the example to seee the rectangle diagrams
for x in range (Rows):
    for y in range(Cols):
        print(Symbol,end = "")
    print()
#Square Patterns
for x in range(8):
    for y in range(8 ):
        print(Symbol, end = " ")
    print()
#this gives a right angle triangle
for i in range(1,6):
    for x in range(i):
        print("#%",end = " ")
    print()
for i in range(1,6):
    for x in range(1,i+1):
        print("#",end = " ")
    print()
#program for reveverse triangle
for i in reversed(range(0,6)):#f
    for x in range(i):
        print("%",end = " ")
    print()

#Program for Numbered Triangle
for i in range(1,6):
    for x in range(1, i + 1):
        print(x, end = " ")
    print()
#Numbered Square pattern
for i in range(6):
    for x in range(6):
        print(x, end = " ")
    print()

#Multiplication Tables
for i in range(16,20):
    for x in range(1,11):
        print(f"{i} *{x} = {i *x}")#print(i * x)#print(i * x, end = " ")#print(i * x, end = "\t")
    print()

for i in range(6):
    for x in range(1, i + 1):
        print(x, end = " ")
    print()
#Finding the prime
for i in range(2,51):
    is_prime = True
    for x in range(2,i):
        if i % x == 0:
            is_prime = False
            break
    if is_prime:
        print(i)
for x in range (1,11):
    if x == 3:
        continue
    print(x)

for x in range(0,51):
    is_prime = True
    if x < 2:
        continue
    for y in range(2, x):
        if x % y == 0:
            is_prime = False
            break
    if is_prime:
        print(x)
#Factors for Primes are 1 and itselt
for x in range(2,51):
    count = 0
    for y in range(1,x+1):
        if x% y == 0:
            count += 1
    if count == 2:
           print(x)
#Multiplication Grid
for i in range(2, 9):
    for y in range(2,9):
        print(i * y, end = " ")
    print()
#this is rect not square
for i in range(6):#because outer for loop has 6 iterations from 0
    for x in range(1,3):#for x in range(6):
        print("%", end = "\t")
    print()
#FLoyd's Triangle
num = 1

for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print() 
num = 1

for i in range(1,6):
    for j in range(1,i+1):
        print(num, end=" ")
        num += 1
    print() 
#Palindrome Number Pattern

for i in range(1, 6):

    for j in range(i, 0, -1):

        print(j, end="")

    print()
rows = 5
#Pyramid Pattern
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()