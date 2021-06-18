#1.Create a function getting two integer inputs from user. & print the following:

def mylist():
    x=int(input("enter the first number="))
    y=int(input("enter the second number="))
    z=x+y
    print("the addition of two numbers=",z)
    z=x-y
    print("the subtraction of two numbers=",z)
    z=x*y
    print("the multiplication of two numbers=",z)
    z=x//y
    print("the division of two numbers=",z)
mylist()
#add sub
def arthi(x,y):
    c=x+y
    d=x-y
    a=x*y
    b=x/y
    return c,d,a,b
result1, result2,result3,result4=arthi(10,2)
print(result1,'\n',result2 ,'\n',result3 ,'\n',result4 ,'\n')



#2. create following covid() & it should accept patient name,and body temperature,by default the body temperature should be 98 degree
def covid(q,w):
    print("patient name is :",q,"\tbody temperature:",w)

q = input("enter patients name:\n")
m = input("enter temperature :")
if m.isalpha() == True:
    w = 98
else:
    w = m
covid(q,w)