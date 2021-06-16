#1)Write a program to create a list of n integer values and do the following

#Add an item in to the list (using function)
a=[1, 3, 5, 7, 9]
a.append(6)
print(a)

#Delete (using function)
b = [1, 2, 3, 4, 5]
del b[3]
print(b)

#Store the largest number from the list to a variable
#Store the Smallest number from the list to a variable
c= [19,23,4,9,5]
lo = min(c)
hi = max(c)
print(lo)
print(hi)

#2)Create a tuple and print the reverse of the created tuple
a =(1, 4, 5, 7, 9)
b=reversed(a)
print(tuple(b))

#3)a tuple and convert tuple into list
a =(1, 4, 5, "hola" ,7, 9,"bye")
b=list(a)
print(list(b))

