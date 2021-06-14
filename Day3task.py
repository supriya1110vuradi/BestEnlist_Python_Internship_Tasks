#Day 3 – Python Programming - Simple Registration form

#importing library
from tkinter import *
from tkinter import ttk

#Creating object 'window' of Tk()
window = Tk()

#Declaring Window Title
window.title("Employees Registration Form")

#Declaring Window size
window.geometry('650x500')

#Declaring Window Color
window.configure(background = "light pink");

#below 12 fields are declared
#label
Heading = Label(window ,text = "Fill the details", width= "10", bg="light blue", fg= "black", font=("bold",14)).grid(row = 0,column = 2)
Firstname = Label(window ,text = "First Name:", bg="light pink", font=("bold",13)).grid(row = 1,column = 0)
Middlename= Label(window ,text = "Middle Name", bg="light pink", font=("bold",13)).grid(row = 2,column = 0)
LastName = Label(window ,text = "Last Name:", bg="light pink", font=("bold",13)).grid(row = 3,column = 0)
Mobile = Label(window ,text = "Contact Number:", bg="light pink", font=("bold",13)).grid(row = 4,column = 0)
EmployeeId= Label(window ,text = "Employee Id:", bg="light pink", font=("bold",13)).grid(row = 5,column = 0)
Email = Label(window ,text = "Email Id:", bg="light pink", font=("bold",13)).grid(row = 6,column = 0)
Address= Label(window ,text = "Address:", bg="light pink", font=("bold",13)).grid(row = 7,column = 0)
Qualifications= Label(window ,text = "Qualifications:", bg="light pink", font=("bold",13)).grid(row = 8,column = 0)
Designation = Label(window ,text = "Designation:", bg="light pink", font=("bold",13)).grid(row = 9,column = 0)

#radio botton
var=IntVar()
Gender =Label(window ,text= "Gender:", bg="light pink", font=("bold",13)).grid(row = 10,column = 0)
Radiobutton(window,text="Male",padx= 10, variable= var, value=1, bg="white", font=("bold",10)).grid(row = 10,column = 1)
Radiobutton(window,text="Female",padx= 20, variable= var, value=2, bg="white", font=("bold",10)).grid(row = 10,column = 2)

#dropbox list
Country=Label(window,text="Country:", bg="light pink", font=("bold",13)).grid(row=11, column=0)
#this creates list of countries available in the dropdownlist.
list_of_country=[ 'India' ,'US' , 'UK' ,'Germany' ,'Austria']

#the variable 'c' mentioned here holds String Value, by default ""
c=StringVar()
droplist=OptionMenu(window,c, *list_of_country)
droplist.config(width=18, bg="white", font=("bold",9))
c.set('Select your Country')
droplist.grid(row= 11, column= 1)

#this will accept the input string text from the user.
Firstname1 = Entry(window).grid(row = 1,column = 1)
Middlename1=Entry(window).grid(row=2, column=1)
Lastname1 = Entry(window).grid(row = 3,column = 1)
Mobile1 = Entry(window).grid(row = 4,column = 1)
EmployeeId1= Entry(window).grid(row = 5, column =1)
Email1 = Entry(window).grid(row = 6,column = 1)
Address1= Entry(window).grid(row = 7,column = 1)
Qualifications1= Entry(window).grid(row = 8,column = 1)
Designation1= Entry(window).grid(row = 9,column = 1)

#fubction declaration
def clicked():
    res = "Welcome to " + txt.get()

Button(window ,text="Submit", fg="black",bg="Light blue", font=("bold",9), command = clicked).grid(row=16,column=2)
window.mainloop()

