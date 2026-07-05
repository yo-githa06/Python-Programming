# Lambda function with other buit in functions like map(), filter().sorted()
# map:The map() function applies a function to every item in an iterable:
n = int(input("Enter a number: "))
numbers = [7,9,5,5,7,8]
Result = list(map(lambda x : x * n, numbers))
print(Result)
#eg
N = int(input("Enter a number: "))
def outer(N):
    return lambda X : X * N
multiply = outer(N)
print(multiply(6))

#val = outer(8) #is for n
#print(val(2))
# lambda function with filter() that prints only the ug'
UG= ["SSC","IPE","University","JNTU","OU"]
result =list(filter(lambda Ans : Ans != "SSC" and Ans != "IPE",UG))
print(result)

Nums = [9,8,7,6,5,4,3,2,1]
result = list(filter(lambda A : A %2 == 0, Nums))
print(result)

Numer = [("Yogitha",19),("Devnder",49),("Shirisha",39),("Sai Teja",21)]#list of tuples
result = sorted(Numer, key = lambda X : X[0])
print(result)



# List sorting
Courses = ["Data Analystics","Data Science","Machine learning","Artificail Intelligenc"]# sorts Alphabetical order
Courses.sort(reverse= True)# prints in reverse order ie., Descending
print(Courses)

# customizing the sorting is using the the keyword argument
#The function will return a number that will be used to sort the list(the lowest number first )
def myfunc(n):
    return abs(n-50)
Nums = [90,65,98,89,55]
Nums.sort(key = myfunc)# prints the number form lowto high which are near to the number 50
print(Nums)
# in list we can use case sensitive functions as key functions like 

Skills = ["Python","mySQl","PowerBI","data Visualisation","statistics","Excel"]
#Skills.sort(key = str.lower)#here the buit in functions are used as key functions#
Skills.reverse()
print(Skills)

# List copy 
Domains = ["Finance","Agriculture","Software","Hardware","Business"]
Copy_cat = Domains[:]#opy_cat= Domains.copy()#Copy_cat = list(Domains)# Copy_cat = Domains[:]
print(Copy_cat)

#List appending(Concatinating or adding)
Lis1 = ["Yo","Yo","Yogi","yogitha"]
Lis2 = [2,2,4,7]
#print(Lis1 + Lis2)#method1
#for i in Lis2:#method2
    #Lis1.append(i)
#print(Lis1)
#Lis1.extend(Lis2)#method3
#print(Lis1)
print(Lis1.count("Yo"))

#Recursion function:A function call itself is called as recursion function it has a meaning that a the loop results in required
#program for Countdown
def recur(n):
    if n <= 0:#base case which have stops the recursion
       print("Done!")
    else:
        print(n)
        recur(n-1)#recursive case ie a function calls itself with a modified argument
print(recur(7))


# factorial
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(7))

#Fibonacci: it is a sequence of a pattern where each number in teh sequesne is the sum of the two preceeding numbers
def fibonacci(n):
    if n <= 1:
        return n 
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(7))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))# only use return Type not print
print(fibonacci(8))

# Checking the recursion limit in python:
import sys
print(sys.getrecursionlimit())

# FIndinh the sum of list of numbers,here recursion process the list by handling one element at a time
def Sum_list(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + Sum_list(numbers[1:])
list = [1,2]
print(Sum_list(list))

def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2]
print(sum_list(my_list))

#Finding the max number from the list
def Max(nums):
    if len(nums) == 0:
        return nums[0]
    else:
        select = Max(nums)
        return nums[0] if nums[0] > select else select
