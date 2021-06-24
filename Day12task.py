#Create a file 30 days 30 hour operations
#Write data in it I have completed 10 days successfully.
#Append the data your name in to it.
#Close the file.


file1 = open(r"C:\Python\Python36\30days30hours.txt","w+")
file1.write("I have completed 10 days successfully")
print(file1.read())
file1.close()

file1 = open(r"C:\Python\Python36\30days30hours.txt","a")
file1.write("\n Supriya")
file1.close()
