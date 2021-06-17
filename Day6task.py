#1) Write a Python script to merge two Python dictionaries
Colors1 = {"Pink":"Purple",
          "Blue":"Violet",
          "Black":"White"}
Colors2 = {"Orange":"Yellow",
           "Red":"maroon",
           "Brown":"Green"}
Colors1.update(Colors2)
print(Colors1)

#2) Write a Python program to remove a key from a dictionary
Colors1 = {"Pink":"Purple",
          "Blue":"Violet",
          "Black":"White"}
del Colors1["Pink"]
print(Colors1)

#3) Write a Python program to map two lists into a dictionary
num = ["1", "2", "3"]
Colors = ["Pink", "Blue", "Black"]
a = dict(zip(num, Colors))
print(a)

#4) Write a Python program to find the length of a set
set={"Hello", "Hey", "Hola", "Hi", "Heya"}
print(len(set))

#5) Write a Python program to remove the intersection of a 2nd set from the 1st set
set1 = {"100", "200", "300", "400", "600"}
set2 = {"700", "850", "200", "100", "900"}
print(set1)
print(set2)
set1.difference_update(set2)
print(set1)
