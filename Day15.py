#List COmprehension: This is the concise way to create a new list in python which is compct and easy to undersatnd than loops in python with shorter sys=ntax
veg = ["Egg","Chicken","Paneer","Potato"]
#Non veg= [X for X in veg if "Chicken" in X]# Prints only CHikcne
#newlist = [X for X in veg if "Chicken" not in X]# Prints the whole old list excepy Chicken
#newlist = [X for X in veg]# prints new list
#newlist = [X if X != "Chicken" else "Mushroom" for X in veg]# To print Mushroom Insted of chicken keed a condition in the Expression
#upp =[X.capitalize() for X in veg]
#upp =[X.capitalize() for X in veg]
first =[x[0] for x in veg]

#print(newlist)
#print(upp)
print(first)


print(newlist)

Double = [1,2,3,4,56,7,8,9]

#new = [X * 2 for X in range(1,22)]
new = [X // 2 for X in Double if X > 5]# prints only the Numbers that are greater than 5
print(new)
Skill = ["Python","SQl","DSA","Libraries","Excel","PowerBi","Statistics","Visuliasation"]
ne = ["Loading" for x in Skill]
print(ne)

'''
# Positive nums 
Nums = [2,-4,6,9,-3,8,-1,0]
#positive= [X for X in Nums if X >= 0]
#negative = [X for X in Nums if X <= 1]
#zero_exclude = [X for X in Nums if X != 0]
even = [X for X in Nums if X %2 == 0 ]
#print(positive)
print(even)
#print(negative)
#print(zero_exclude)
Age = [12,4,6,78,89,5,87,34,21,54,9,6]
ans = [X for X in Age if X > 18]
print(ans)
#match case :Match case is used to perform different actions based on diffrent conditions
#Instead of writing many if..else statements, you can use the match statement.
#The match statement selects one of many code blocks to be executed.
Day = int(input("Enter a number from (1-7) to determine your weekday: "))
match Day:
    case 1:
        print("Monday")
    case 2:
        print("Tueday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
#if there are no matching cases there, we use _ at the last case if thre is no other match cases left
#The match case evaluates the expression only once and compared with the valies of the case
CGPA = int(input("ENter your CGPA marks you got(1 to 10): "))
match CGPA:
    case 1:
        print("Failed")
    case 2:
        print("Bad")
    case 3:
        print("Worst")
    case 4:
        print("Basic")
    case 5:
        print("Average")
    case 6:
        print("Above Avg")
    case 7:
        print("good")
    case 8:
        print("very Good")
    case 9:
        print("Brave")
    case 10:
        print("Excellent")
    case _:
        print("Invalid,Recheck Again!")'''#this is the default case in python which executwes a s a default case

#Generators are the functions that can pause & resume theur execution
def Generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
for num in Generator():
    print(num)
print()
def Generator(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for i in Generator(5):
    print(i)

for i in range(10):
    print(i)

name = "yogitha"
for k in (name):
    print(k)
print(k)#prints the last value

age = 19
for k in range(age):
    print(k)
print(k)#the final result

'''Sum = 0
while True:
    if age != 0:
        for y in range(age):
            Sum += y
        print(Sum)
    else:
        break
print(Sum)'''
Sum = 0
for j in range(age):
    Sum += j
    print(Sum)
print(Sum)

def Generator(n):
    count = 1
    while count <=  n:
        yield count
        count += 1
for i in Generator(7):
    print(i)