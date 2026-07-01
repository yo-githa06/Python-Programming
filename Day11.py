#A Functions is block of reusable code by placing() after a function to invoke it functions make reusablity and also efficient etc
def Python_desc(desc):# Parameters are passed while defining function like variables
    print("Actively learning Python")
    print(f"learning python is giving me sort of Confident and {desc}")
    print("Merely Python is one of the easiest program language")
#to print all the above statement for man or secific no of times withot loops we use Functions and just invoke to print it
Python_desc("Selflessness")#invoking Function
#to functions inputs data is sent as arguments while nvoking

def parcel_status(Order,Place,delivery,payment,Shipping):
    print(f"Your order {Order} out for shipping for {Shipping} ")
    print(f"Congrats on ur {delivery} delivery")
    print(f"you choosed {payment} to pay after reaching {Place} ")
parcel_status("Dress","Yapral","Free!","Cash on delivery","Hyderabad")


def Finance(Analysis,Export,Import):
    print(f"There was drastic {Analysis} in the market")
    print(f"There are exports {Export}")
    print(f"The imports are{Import}")
Finance("Increase","OutDate","Update")

#Return: Statement which is used to end a function
#and send result back to the caller
def add(X,Y):
    Z = X + Y
    return Z
print(add(20,30))

def Subtract(K,L):
    M = K - L
    return M
print(Subtract(233,122))

def Avg(x,y,z,k,l,m,n):
    result = x+y+z+k+l+m+n
    Ans = result // 7
    return Ans

print(Avg(2,3,9,2,8,9,4))

def Indoor(Sit,Stand):
    Sit = Sit.capitalize()
    Stand = Stand.capitalize()#this attribute will make the 1st wrod of value capital and rest lowers
    Game = Sit + "      " + Stand
    return Game
print(Indoor("Carroms, Chess",  "table tennis,SKIPPING"))

#Default Arguments are majorly used for certain parameters
#Default is used when that argument is Omitted while invoke a function 
def Selling_price(manufprice, Discount,tax):
    return manufprice*(1 - (Discount/100)) * (( 1 + (tax/100)))
    

print(Selling_price(9000,20,5))

def net_price(listprice,Discount = 0.1 ,Tax = 0.5):#thesea re set to as Default parameters
    return listprice * (1 - Discount) * (1 + Tax)

print(net_price(1000,0,0.8))#if passed any argument to the function then the passed value is considered not the default
print(net_price(1000,0.9,0))

#Counter Time program
import time
def count_down(end,Start = 0):#default paramets are followed by non default once while declaring variable
    for i in range(Start,end):
        print(i)
        time.sleep(0.2)
print()
#count_down(1,20)
#count_down(10,0)
#count_down(3)Always a parameter without a default follows parameter default error 
count_down(30)
#Hence default arguments are more flexiblea nd reduces the no of args t0 pass'''

#Keyword Arguments
#These args are prceded by an identifier, order of argument doesn't matter improves readability

def Feel(Disappoint,Lazy,happy,Fail):
    return (f"Your really {Disappoint},{Lazy},{happy},{Fail} Sometimes")

print(Feel("Upset","Unable","Overwhlemed","Sorrow"))# prints all in order
#print(Feel("Disappoint","Upset","Joy","Unable"))#print in order
#print(Feel(Disappoint = "Upset",Lazy = "Unable",happy = "Joy",Fail = "Loose"))# preceeding the values with the parameters
#print(Feel("Sad",Lazy= "Upset","Joy",Fail = "Loose",))#Always Positional args shld follow keyword args
#print(Feel("Upset",Lazy = "Dull",Fail = "Losse"happy = "Joy",))#order not matters andposiitonal args are first the pass the keywords


for i in (1,9):
    print(i , end = " ")

def Codes(Continent,Country,State,City,District = "Medchal"):
    codes = (f"I am in {Country} which is in {Continent} in {State} in {District} in {City}")
    return codes

print(Codes("Asia",Country = "india", City = "Hyderabad",State = "Telangana",))