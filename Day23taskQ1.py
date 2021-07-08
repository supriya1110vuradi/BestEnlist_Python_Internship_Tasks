#1.Create a browse option with a specific folder which has all the JPEG Files & create a Convert button to convert the image from JPEG to PNG – Basic Image converter App
# import all prerequisite
from tkinter import *
from tkinter import filedialog as fd
import os
from PIL import Image
from tkinter import messagebox

root = Tk()

# naming the GUI interface to image_conversion_APP
root.title("Basic_Image_Convertor_App")
root.configure(background = "pale violet red")

# creating the Function which converts the jpg_to_png
def jpg_to_png():
	global im1

	# import the image from the folder
	import_filename = fd.askopenfilename()
	if import_filename.endswith(".jpg"):

		im1 = Image.open(import_filename)

		# after converting the image save to desired
		# location with the Extersion .png
		export_filename = fd.asksaveasfilename(defaultextension=".png")
		im1.save(export_filename)

		# displaying the Messaging box with the Success
		messagebox.showinfo("success ", "your Image converted to Png")
	else:

		# if Image select is not with the Format of .jpg
		# then display the Error
		Label_2 = Label(root, text="Error!", width=20,
						fg="red", font=("bold", 15))
		Label_2.place(x=120, y=280)
		messagebox.showerror("Fail!!", "Something Went Wrong...")


def png_to_jpg():
	global im1
	import_filename = fd.askopenfilename()

	if import_filename.endswith(".png"):
		im1 = Image.open(import_filename)
		export_filename = fd.asksaveasfilename(defaultextension=".jpg")
		im1.save(export_filename)

		messagebox.showinfo("success ", "your Image converted to jpg ")
	else:
		Label_2 = Label(root, text="Error!", width=20,
						fg="red", font=("bold", 13))
		Label_2.place(x=80, y=280)

		messagebox.showerror("Fail!!", "Something Went Wrong...")

welcome = Label(root ,text = "Welcome to Basic Image Convertor App", width= "35", height=1, bg= "thistle1", fg= "black", font=("helvetica", 15, "bold"))
welcome.place(x=50, y=10)

label1 = Label(root ,text = "Convert JPG to PNG:", bg= "pale violet red", font=("helvetica", 14, "bold"))
label1.place(x=120, y=90)
label2 = Label(root ,text = "Convert PNG to JPG:", bg="pale violet red", font=("helvetica", 14, "bold"))
label2.place(x=120, y=190)

button1 = Button(root, text="JPG_to_PNG", width=25, height=2, bg="light pink",
				fg="dark blue", font=("helvetica", 12, "bold"), command=jpg_to_png)

button1.place(x=120, y=120)

button2 = Button(root, text="PNG_to_JPEG", width=25, height=2, bg="light pink",
				fg="dark blue", font=("helvetica", 12, "bold"), command=png_to_jpg)

button2.place(x=120, y=220)
root.geometry("500x500+400+200")
root.mainloop()
