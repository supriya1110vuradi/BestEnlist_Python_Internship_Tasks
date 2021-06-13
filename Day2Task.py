#Day 2 : String Practice

#How to print a value?
print("30 days 30 hour challenge")
print('30 days 30 hour challenge')

#Assigning String to Variable:
Hours = "thirty"
print(Hours)

#Indexing using String:
Days = "Thirty days"
print(Days[3])

#How to print the particular character from certain text?
Challenge = "I will win"
print(Challenge[5:10])

#Print the length of Character:
Challenge = "I will win"
print(len(Challenge))

#Convert String into lower character;
Challenge = "I will win"
print(Challenge.lower())

#String Concatenation – Joining two strings
a = "30 Days"
b = "30 hours"
c = a + b
print(c)

#Adding space during concatenation
a = "30 Days"
b = "30 hours"
c = a + " " + b
print(c)

#casefold() - Usage
text = "Thirty days and Thirty hours"
x = text.casefold()
print(x)

#capitalize
text = "DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU"
x = text.capitalize()
print(x)

#find
text = "DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU"
x=text.find("TROUBLE")
print(x)

#isalpha
text= "DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU"
x=text.isalpha()
print(x)

#isalnum()
text="DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU"
x=text.isalnum()
print(x)

#Output:
30 days 30 hour challenge
30 days 30 hour challenge
thirty
r
l win
10
i will win
30 Days30 hours
30 Days 30 hours
thirty days and thirty hours
Don’t trouble trouble until trouble troubles you
6
False
False
