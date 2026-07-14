#RegEx is a regular expression where a sequence of characters which formsa serch pattern on string fr a match/ RegEx can be used to check if a string contains the specified search patter
#so here came module called re built in python package
#We have metacharacters which have a spacial meaning 
import re
State = "Yogitha is a very good girl in this whole world ad she is 19 year old"
'''res = re.search("^Yogitha.*world", State)
if res:
    print("Yes it is right")
else:
    print("Wrong!")'''
'''res = re.findall("^Yogitha",State)#Returns a list containing all matches findall() function  while chaking if the string starts with Yogitha
if res:
    print(res)
else:
    print("Wrong")'''
'''res = re.search(f"world$",State)
if res:# we used findall functiona and $ is the metacharacter which  seaches to check if the string ends with 
    print("Yes! Right")
else:
    print("Wrong")'''
'''res = re.findall(f"Yo.*is", State)# * is a metacharacter which seaches fro a sequence that starts with Yo and have 0 or more anything and results in( zero or more occurances)
print(res)
if res:
    print("Yes! Correct")
else:
    print("Wrong")'''
'''res = re.findall("[A-Z]", State)#a set of characters returns the list with the Upper case characters b/w Ato Z
print(res)'''
'''res = re.findall("\d",State)# Signals a special sequence like in this case returns digits numbers
print(res)'''
'''res = re.findall("Yo......is", State)# this returns the string that starts with Yo and 6 characters includiing the spaces and also an is using the . metacharactert returns any character between
print(res)'''
#search function retuns the match object
'''res =re.search("wo.*s",State)#This returns zero or more occcureb=nces in between the wo and d
res =re.findall("wo.*s",State)
print(res)'''
'''res = re.findall("Yo.+c",State)# prints nothing since ther is no c in the string
res = re.findall("Yo.+n",State)#This returns the string that have one or more occurences using +
print(res)'''

'''res = re.findall("Yo.?n",State)#this retruns string that have zero or one occurencesusing ?
print(res)'''
#RegEx has functions like fidall() which returns the list of the match objects,search() which returns the match objects,Split()which returns the list where the string i split at each match,sub() which replaces the matches with the text or strings
#findall()
State = "Yogitha is a very good girl in this whole world ad she is 19 year old"
'''X = re.findall("[A-Z]", State)
print(X)'''
#search()
#X = re.search("is", State)
'''X = re.search("^oo",State)
print(X)
# split()this returns the slist and splits the string at each match
X = re.split("\s",State,8)# we can also control the no of occurences
print(X)'''
X = re.split("^Yogitha",State,)
print(X)
X = re.sub("Yo.*old","Yogitha is a very goood girl",State)
print(X)
X = re.sub("\s","_",State,15)
print(X)



#Pip in python package manager for modules , and packages which are not in the standard library of python and can be installed using pip
'''import camelcase
Name = "yogitha doodimadugula"
c = camelcase.CamelCase()
print(c.hump(Name))# returns the first letter of each word to be capitalised, WHere hump is a method used to convert a string to Camelcase'''
import camelcase
name = "yogitha doodimadugula"
c = camelcase.CamelCase()
print(c.hump(name))

# Note Python has modules or packages like random,Date,Math,Json which holds various methods and functions to work with the data and also to perform various operations on the data