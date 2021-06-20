#1]Write a Python script to merge two Python dictionaries
#method1
color_a={"color1":"pink", "color2":"red", "color3":"blue", "color4":"purple", "color5":"violet"}
color_b={"color6":"brown", "color7":"black", "color8":"white"}
color_a.update(color_b)
print(color_a)

#method2
color_c={**color_a, **color_b}
print(color_c)


#2]Write a program to sort the value from descending to ascending in list and convert it in to a set.
list=[56, 45, 89, 34, 23, 67,34]
list.sort()
print(list)
print(set(list))


#3]Write a Python program to list number of items in a dictionary key and sort the list with the help of a function & without the function.
dict1={'Divi':[12,13,21,16],'Renu':[12,67,54,43],'Shri':[34,87,88,98],'Anu':[33,66,55,44]}
result={k:sorted(dict1[k]) for k in sorted(dict1)}
print(result)

dict1={'jeryy':[12,13,21,16],'Tom':[12,67,54,43],'Sam':[34,87,88,98],'Elon':[33,66,55,44]}
def function1(dict1):
    res = dict()
    for key in sorted(dict1):
        res[key] = sorted(dict1[key])
    return res
print(function1(dict1))

#4]Write a Python program to find the repeated items of a list
a =[10, 20, 30, 10, 40, 30, 50, 20, 60, 70, 40]
b=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        print(i, end=' ')


#5]Write a Python program to find the Mean,median,mode among three given numbers
a= [45, 56, 56]
b= len(a)
c=sum(a)
mean =c/b
print("mean is" +str(mean))
a.sort()
if b%2==0:
    med1=a[b//2]
    med2=a[b//2-1]
    median=(med1+med2)/2
else:
    median=a[b//2]
print("median is:" +str(median))

#mode
def mode(lists):
    mode=max(lists, key=lists.count)
    return mode
print(mode([45, 56, 45]))


#6]Write a Python program to get a string from a given string where all occurrences of its first char have been changed to capital letter.
a = input("Enter a string:")
print(a.capitalize())


#7]Write a Python program to check the sum of three elements and divided by a value which is given as an input by the user
a=int(input("Enter the value a :"))
b=int(input("Enter the value b :"))
c=int(input("Enter the value c :"))
sum=a+b+c
print(sum)
d=int(input("Enter the number to divide sum:"))
if sum% d==0:
    print("The given input divide")
else :
    print("The given input does not divide sum")
#or
a=int(input("Enter the value a :"))
b=int(input("Enter the value b :"))
c=int(input("Enter the value c :"))
sum=a+b+c
print(sum)
d=int(input("Enter the number to divide sum:"))
sum1 = sum/d
print(sum1)


#8]Write a Python program to swap cases of a given string
#method1
string="Hello World"
print(string.swapcase())

#different_method1
a="Python"
b="World"
temp=a
a=b
b=temp
print(a,b)

#different_method2
a="Python"
b="World"
x = a
y = b
x, y = y, x
print(x,y)


#9]Write a program to convert an integer to binary & octa decimal
a = 45
print(bin(a))
print(oct(a))


#10]Write a Python program to get a string from a given string (user input) and change the first occurrence of the word to a user specified input.
#method1
def fun():
    user_input=input("Enter the string :")
    sentence="Python world"
    return user_input+sentence[6:]
print(fun())

#method2
def fun():
    user_input=input("Enter the string :")
    sentence="Python world"
    return sentence.replace('Python', user_input)
print(fun())

