
#Unpacking List with*
def Some(a,b,c):
    return a +b +c
numbers = [1,2,3]
print(Some(*numbers))

#Unpacking List with**
def Soming(lname,lage):
    print("Hello",lname,lage)
person = {"lname":  "Yogi","lage": "10"}
print(Soming(**person))


#Scope:A Variable that can be accesed within a region is called a scope
def func():
    x = 10
    print(x)
func()
#print(x)The scope of x is within the function func
#Local Variable
x = 10
def Local():
    x = 2000
    print(x)
print(x)
Local()
X = 300
def global_assign():
   # X += 1 #can't make changes to the function 
    print(X)
print(X)
global_assign()

# to make a variable gloabal use glaobal keyword a
global Y 
def eg2():
    Y = 900
    print(Y)
eg2()


Name = "Doodimadugula"
def Full_name():
    global Name#the value of the variable can be change sing the gloab;l keyword and works only to the scopeof that fuction
    Name = "Yogitha"
    return Name 
print(Name)
print(Full_name())

# to work with the variable in the inner functiona or to make it belong to the outer function also we use the nonlocal keyword
def Non():
    cat = "Meoms"
    def logal():
        nonlocal cat
        cat = "mammal"
    logal()
    print(cat)
Non()


#Python follows a rule called as the LEGB ie., while looking or searching for any variable in the code
#lEGB= local,Enhancing(both outer and inner functions),Global,Built in python
R = "Global"
def Outer():
    R = " Outer Enclosing"
    def inner():
        R = "Inner Enclosing"
        print("Inner,R")
    return inner()
    print("Outer:",R)
Outer()
print("Global:",R)
# Decorator 
#A Decorator is function that takes another decorator as input an returns new function , also adds extra behavior to the function without changeing the code of the function
#Add the @ decoratername above the function name which need to be decorated


def changeCase(func):
    def outer():
        return func().upper()
    return outer()

@changeCase
def action():
    return "Yogitha"
print(action())
    
def indexing(ret):
    def func():
        return ret().index(" ")
    return func

@indexing
def result():
    return "D Yogitha"
print(result)

# Argumnets are also passed in the decorated function
def indexing(ret):
    def func(k):
        return ret(k).lower()
    return func


@indexing
def actioning(age):
    return "Yogitha" + "is" + "good girl, her age is " + age
print(actioning("19"))

# Multiple Decorator calls
def multiple(func):
    def inner(c):
        return func(c).upper()
    return inner

    
@multiple
def actions(ans):
    return "you are right and got " + ans 
print(actions("20"))
@multiple
def actions2(res):
    return "you are wrong and got " + res
print(actions("20"))
print(actions2("1"))

#Metadata in python like _name_ and _doc_
def Yogitha():
    return good
print(Yogitha.__name__)# the __name__ and __doc__ are the two attributes in python gives thename of the function

#For decorateed functions
def changecase(func):
    def outer():
        return func().upper
    return outer

@changecase
def inner():
    return "Yogitha is Clever"
print(inner.__namer__)# the function metadata is lost when it is decoprated so there isa buit in fuction launched called as functools.wrap preserves metadata

import functools
def changecase(A):
    @functools.wraps(A)
    def outer():
        return A().Capitalise()
    return outer

@changecase
def inner():
    return "Yo you speed is growing"
print(inner.__name__)


#Lambda Functions
A = lambda B : B + 8
print(A(12))

def Big(x):
    return lambda a : a * x
declaring = Big(3)#declare value for x
declare = Big(7)#declare value for x

print(declaring(6))# gives the value for a
print(declare(2))# gives the value for a
