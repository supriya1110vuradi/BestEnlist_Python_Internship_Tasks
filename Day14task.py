#List down all the error types and check all the errors using a python program for all errors
# 1 ZeroDivisionError
a = 10
b = 0
print("Result of Division: " + str(a/b))

# 2  IndentationError= in code there is no space near print
site = 'Best'
if site == 'Best':
print('Logging in to Best!')
else:
print('Please type the URL again.')
print('You are ready to go!')

# 3 Type Error
a = 2
b = 'Hello'
a + b

# 4 KeyError
D1={'1':"aa", '2':"bb", '3':"cc"}
D1['4']

# 5 Assertion Error
x = 0
assert x > 0, 'Only positive numbers are allowed'
print('x is a positive number.')

# 6 Index error
L1=[1,2,3]
L1[3]

# 7 Atribute Error:
import sys
try:
    my_list = [3,7, 9, 4, 6]
    print( my_list[6])
except IndexError as e:
    print(e)
    print(sys.exc_type)



#Design a simple calculator app with try and except for all use cases

print("add:")
def addition(num1,num2):
	try:
		result=num1+num2
		print(result)
	except Exception as e:
		print(e)
addition(6,3)

print("subtract:")
def subtract(num1,num2):
	try:
		result=num1-num2
		print(result)
	except Exception as e:
		print(e)
subtract(8,4)

print("divide:")
def divide(num1,num2):
	try:
		result=num1/num2
		print(result)
	except Exception as e:
		print(e)
divide(12,2)

print("multiply:")
def multiply(num1,num2):
	try:
		result=num1*num2
		print(result)
	except Exception as e:
		print(e)
multiply(8,5)



#print one message if the try block raises a NameError and another for other errors
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")



#Try getting an input inside the try catch block
try:
    a = int(input("enter A:"))
    b = int(input("enter B:"))
    c = a / b
except:
    print("cannot be defined")


