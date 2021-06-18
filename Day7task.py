#1.Create a function getting two integer inputs from user.& print the following:
#Addition of two numbers is +value
#Subtraction of two numbers is +value
#Division of two numbers is +value
#Multiplication of two numbers is +value
#Here the value represents math function associated

a=int(input("enter the value 1:"))
b=int(input("enter the value 2:"))
def my_func(x,y): 
    print("Addition of two numbers is",x+y)
    print("Substraction of two numbers is", x-y)
    print("division of two numbers is",x/y)
    print("Multiplication of two numbers is",x*y)
my_func(a,b)


#2.Create a function covid( )& it should accept patient name, and body temperature, by default the body temperature should be 98 degree

def covid(temp):
    print("Body Temperature of Tom is:" +str(temp))
covid(98)
