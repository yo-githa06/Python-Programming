#Iterators can be any objects or are called as the iterable objects ie., Sets, lists,arrays,tuples,dictsetc
#majorly used in the for loops its valuei
# Iterableare objects or collections  that returns each element in the collection called as the iterators
ex = ["Yogitha","Devender","shirsiha","sai teja"]
name = iter(ex)#iterator has 2 methods ie., iter() and next(),with iter()we get thethe iterator from

print(next(name))# this returns each iterator
print(next(name))
print(next(name))

example = "yogitha"
for i in example:
    print(i)
print(i)

print({1,2,3} & {2,3,4})

#Modules in python there are two types like user defined and also built in like random,sys,math etc save the code for the module in the module_name.py file and then import it in that module
#Consider a module to be the same as a code library.
#A file containing a set of functions you want to include in your application.
'''import MyMod
print(MyMod.Mod())

#print()
from MyMod import Dict
result = Dict["Gender"]
print(result)'''

# re-naming the module
import MyMod as Modu
a = Modu.name("39")
print(dir(Modu))
print(a)

import platform 
x = platform.system()
y = dir(platform)
print(x)
print(y)


K = max(2,99)

print(k)
l = min(99,4)
print(l)
z = [3,4,5,77,2,]
print(max(z))

a = 2
b = 3
print(pow(a,b))


#math functions and modules:where the module has various functions and constants in math
import math
x = math.pi
print(x)
y = math.ceil(3.2)
print(y)

#datetime modulethere is a module called datetime to work with dataes objects since there is now data type for this
import datetime
x = datetime.datetime.now()#method in the module of datetime
print(x)   
print(x.year)
print(x.strftime("%a"))#returns half version
#creating the dattime
y = datetime.datetime(2026,6,30,10,21,1)# time is set to 0
print(y)
print(x.strftime("%B"))


#JSON is a syntax that can store and also exchange dsta
#Json is text is majorily written in Javascript object notationLike dicts,lists,tuples,etc
#there is a module called Json to work on json file 
import json
# to parse JSON converts from Json to pytho :Where json.load() is the method which coverts the json files to python
y = '{"Name":"Yogitha","Age":19,"Gender": "Female"}'
result = json.loads(y)
print(result["Name"])
#json.dumps() is a method ie., used to convert the python object to json str
k = {
    "ID":39,
    "Dept":"CyberSecurity",
    "Company":"Deloitte",
    "Salary":"12LPA"
}#converts to objects
Dump = json.dumps(k)
print(Dump)

#json.dumps() is the method that works to convert the python objetcts like List,Tuple,String,Int,True,False,Dicts,and floats
print(json.dumps(["Yogitha","Devender","Shirisha","Sai teja"]))#converts to Arrays
print(json.dumps(("Yogitha","Devender","Shirisha","Sai teja")))#converts to Arrays
print(json.dumps("Yogitha"))#converts to string
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(19))
print(json.dumps(math.ceil(19.8)))
print(json.dumps(None))#null
#print(json.dumps("Yo","Yogi","Official"))

#convert the all the python objects to the json which also accepts all the indentations etc
d = {
    "Name": "Yogitha",
    "Age": 19,
    "Gender":"Female",
    "Class":"Btech",
    "Job":("Tech","Govt"),
    "Distraction":None,
    "cars": [
        {"Salary":100000,
            "Debts":400000,
            "Model":"Mahindra"
            },
            {"Contribute":"Parents","Major": "Self","Mode":"Online"}
             ]
             }
k = json.dumps(d,indent = 3,separators = (".","= "), sort_keys= True,)
print(k)