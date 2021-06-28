#Create a lambda function that multiplies argument x with argument y
a = lambda x, y: x * y
print(a(11, 12))

#Write a Python program to create Fibonacci series to n using Lambda
from functools import reduce
fib_numbers = lambda y: reduce(lambda x, _: x + [x[-1] + x[-2]], range(y - 2), [0, 1])
print(fib_numbers(10))

#Write a Python program that multiply each number of given list with a given number
a =[1, 2,3,4,5]
n= 4
multi = list(map(lambda a: a * n, a))
print(multi)

#Write a Python program to find numbers divisible by 9 from a list of numbers
a = [9, 18, 63, 81, 45, 27, 53]
b = 9
divid = list(filter(lambda n: (n % b == 0), a))
print(divid)

#Write a Python program to count the even numbers in a given list of integers
no = [1, 2, 4, 6, 8, 9, 10, 16]
even = len(list(filter(lambda x: (x % 2 == 0), no)))
print(even)
