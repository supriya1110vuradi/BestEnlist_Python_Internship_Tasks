#1]Write a program to loop through a list of numbers and add +2 to every value to elements in list
a=[1, 2, 3, 4, 5, 6, 7]
b=[x+2 for x in a]
print(b)


#2]Write a program to get the below pattern
# 54321
# 4321
# 321
# 21
# 1
c=5
for i in range(c):
    for j in range(c):
      d= c-j
      print(d, end=" ")
    print()
    c-=1


#3]Python Program to Print the Fibonacci sequence
a=0
b=1
n=20
sum1=0
while sum1<=n:
    print(sum1)
    a=b
    b=sum1
    sum1=a+b
    

#4]Write a program to print the multiplication table of 9
for i in range(11):
    table = 9 * i
    print(table)
    
#5]Write a program to convert the number of days to ages
days = int(input("Enter the number of days : "))
a = int(days / 365)
print("Number of years is :" +str(a))


#6]Check if a program is negative or positive
a = int(input("Enter the number:"))
if a>=0:
    print("It's a positive number")
else:
    print("It's a negative number")


#7]Solve Trigonometry problem using math function write a program to solve using math function
import math
print(math.sin(math.pi/3))

#8]Create a calculator only on a code level by using if condition (Basic arithmetic calculation)
print("CALCULATOR")
print("Addition")
print("Subtraction")
print("Multiplication")
print("Division")

a=int(input("Enter a choice value (1-4): "))
if a==1:
      b=int(input("enter a value"))
      c=int(input("enter a value"))
      d=b+c
      print("Addition:", d)
elif a==2:
      b=int(input("enter a value"))
      c=int(input("enter a value"))
      d=b-c
      print("subtraction:", d)
elif a==3:
      b=int(input("enter a value"))
      c=int(input("enter a value"))
      d=b*c
      print("Multiplication:", d)

elif a==4:
      b=int(input("enter a value"))
      c=int(input("enter a value"))
      d=b/c
      print("Division:", d)
else:
      print("Invalid choice")


#9]Explain Armstrong number and write a code with a function
#(4*4*4)+(0*0*0)+(7*7*7)=407

          # Python Program For Armstrong Number using Functions
 
def Armstrong_Number(Number):
           # Initializing Sum and Number of Digits
           Sum = 0
           Times = 0
 
           # Calculating Number of individual digits
           Temp = Number
           while Temp > 0:
                      Times = Times + 1
                      Temp = Temp // 10
 
           # Finding Armstrong Number
           Temp = Number
           for n in range(1, Temp + 1):
                      Reminder = Temp % 10
                      Sum = Sum + (Reminder ** Times)
                      Temp //= 10
           return Sum
#End of Function
 
#User Input
Number = int(input("\nPlease Enter the Number to Check for Armstrong: "))
 
if (Number == Armstrong_Number(Number)):
    print("\n %d is Armstrong Number.\n" %Number)
else:
    print("\n %d is Not a Armstrong Number.\n" %Number)



















