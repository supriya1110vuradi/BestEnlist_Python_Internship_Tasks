#1]Create a connection for DB and print the version using a python program
import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='Sqlpython123#')
if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)

#or
import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Sqlpython123#"
)
print(db_connection)
       
#2]Create a multiple tables & insert data in table.
import mysql.connector
import mysql.connector
db_connection = mysql.connector.connect(
  host= "localhost",
  user= "root",
  passwd= "Sqlpython123#",
  database="records"
  )

#create table
db_cursor = db_connection.cursor()
#Here creating database table as school, college & graduation with primary key
db_cursor.execute("CREATE TABLE student(id INT , name VARCHAR(255), rollnumber INT(2), percentage INT(2))")
db_cursor.execute("CREATE TABLE college(id INT , name VARCHAR(255), rollnumber INT(2), percentage INT(2))")
db_cursor.execute("CREATE TABLE graduation(id INT , name VARCHAR(255), rollnumber INT(2), percentage INT(2))")
#Get database table
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)	


#insert data for school data
	#1
db_cursor = db_connection.cursor()
#Here creating database table as school with primary key
school_sql_query = "INSERT INTO school(id,name,rollnumber,percentage) VALUES(01, 'joey', 67, 78)"
#Execute cursor and pass query as well as student data
db_cursor.execute(school_sql_query)
#Execute cursor and pass query of school and data 
db_connection.commit()
print(db_cursor.rowcount, "Record Inserted")
#Get database table
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)

	#2
db_cursor = db_connection.cursor()
#Here creating database table as  with primary key
school_sql_query = "INSERT INTO school(id,name,rollnumber,percentage) VALUES(02, 'clay', 17, 70)"
#Execute cursor and pass query as well as student data
db_cursor.execute(school_sql_query)
#Execute cursor and pass query of  and data 

db_connection.commit()
print(db_cursor.rowcount, "Record Inserted")
#Get database table
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)	

     #3
db_cursor = db_connection.cursor()
#Here creating database table as  with primary key
school_sql_query = "INSERT INTO school(id,name,rollnumber,percentage) VALUES(03, 'jones', 41, 65)"
#Execute cursor and pass query as well as student data
db_cursor.execute(school_sql_query)
#Execute cursor and pass query of  and data 

db_connection.commit()
print(db_cursor.rowcount, "Record Inserted")
#Get database table
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)	


#Fetch All School data
import mysql.connector
db_connection = mysql.connector.connect(
  host= "localhost",
  user= "root",
  passwd= "Sqlpython123#",
  database="records"
  )

db_cursor = db_connection.cursor()
db_cursor.execute("SELECT * FROM school")
myresult=db_cursor.fetchall()
for x in myresult:
    print(x)



#Insert Data for College table:
    #1
db_cursor = db_connection.cursor()
#Here creating database table 
college_sql_query = "INSERT INTO college(id,name,rollnumber,percentage) VALUES(1, 'Mark', 35, 90)"
#Execute cursor and pass query as well as student data
db_cursor.execute(college_sql_query)
#Execute cursor and pass query of 
db_connection.commit()
print(db_cursor.rowcount, "Record Inserted")
#Get database table
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)

	#2
db_cursor = db_connection.cursor()
#Here creating database table 
college_sql_query = "INSERT INTO college(id,name,rollnumber,percentage) VALUES(5, 'Smith', 50, 45)"
#Execute cursor and pass query as well as student data
db_cursor.execute(college_sql_query)
#Execute cursor and pass query of 
db_connection.commit()
print(db_cursor.rowcount, "Record Inserted")
#Get database table
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)
   
    #3
db_cursor = db_connection.cursor()
#Here creating database table 
college_sql_query = "INSERT INTO college(id,name,rollnumber,percentage) VALUES(11, 'Moon', 5, 75)"
#Execute cursor and pass query as well as student data
db_cursor.execute(college_sql_query)
#Execute cursor and pass query of 
db_connection.commit()
print(db_cursor.rowcount, "Record Inserted")
#Get database table
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)


#Insert Data for graduation table:
    #1
db_cursor = db_connection.cursor()
#Here creating database table 
graduation_sql_query = "INSERT INTO graduation(id,name,rollnumber,percentage) VALUES(1, 'Jerry', 8, 80)"
#Execute cursor and pass query as well as student data
db_cursor.execute(graduation_sql_query)
#Execute cursor and pass query 
db_connection.commit()
print(db_cursor.rowcount, "Record Inserted")
#Get database table
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)

	#2
db_cursor = db_connection.cursor()
#Here creating database table 
graduation_sql_query = "INSERT INTO graduation(id,name,rollnumber,percentage) VALUES(2, 'Tom', 9, 90)"
#Execute cursor and pass query as well as student data
db_cursor.execute(graduation_sql_query)
#Execute cursor and pass query 
db_connection.commit()
print(db_cursor.rowcount, "Record Inserted")
#Get database table
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)
   
    #3
db_cursor = db_connection.cursor()
#Here creating database table 
graduation_sql_query = "INSERT INTO graduation(id,name,rollnumber,percentage) VALUES(11, 'Moon', 5, 75)"
#Execute cursor and pass query as well as student data
db_cursor.execute(graduation_sql_query)
#Execute cursor and pass query of 
db_connection.commit()
print(db_cursor.rowcount, "Record Inserted")
#Get database table
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)



#3]Create a employee table and read all the employee name in the table using for loop
#create table for employee
import mysql.connector
db_connection = mysql.connector.connect(
  host= "localhost",
  user= "root",
  passwd= "Sqlpython123#",
  database="records"
  )

db_cursor = db_connection.cursor()
db_cursor.execute("CREATE TABLE employee (id INT , name VARCHAR(255), salary INT(7))")
#Get database table
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)
	

#insert data into employee
	#1
db_cursor = db_connection.cursor()
#Here creating database table as employee 
employee_sql_query = "INSERT INTO employee(id,name,salary) VALUES(10, 'Kin', 30000)"
#Execute cursor and pass query as well as student data
db_cursor.execute(employee_sql_query)
#Execute cursor and pass query of employee and data of employee
db_connection.commit()
print(db_cursor.rowcount, "Record Inserted")
#Get database table
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)

	#2
db_cursor = db_connection.cursor()
#Here creating database table as employee 
employee_sql_query = "INSERT INTO employee(id,name,salary) VALUES(12, 'chin', 50000)"
#Execute cursor and pass query as well as student data
db_cursor.execute(employee_sql_query)
#Execute cursor and pass query of employee and data of employee
db_connection.commit()
print(db_cursor.rowcount, "Record Inserted")
#Get database table
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)

	#3
db_cursor = db_connection.cursor()
#Here creating database table as 
employee_sql_query = "INSERT INTO employee(id,name,salary) VALUES(14, 'Rim', 40000)"
#Execute cursor and pass query as well as student data
db_cursor.execute(employee_sql_query)
#Execute cursor and pass query of 
db_connection.commit()
print(db_cursor.rowcount, "Record Inserted")
#Get database table
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)

	#4
db_cursor = db_connection.cursor()
#Here creating database table as 
employee_sql_query = "INSERT INTO employee(id,name,salary) VALUES(2, 'Rhea', 60000)"
#Execute cursor and pass query as well as student data
db_cursor.execute(employee_sql_query)
#Execute cursor and pass query of 
db_connection.commit()
print(db_cursor.rowcount, "Record Inserted")
#Get database table
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)

	#5
db_cursor = db_connection.cursor()
#Here creating database table as 
employee_sql_query = "INSERT INTO employee(id,name,salary) VALUES(6, 'king', 25000)"
#Execute cursor and pass query as well as student data
db_cursor.execute(employee_sql_query)
#Execute cursor and pass query of 
db_connection.commit()
print(db_cursor.rowcount, "Record Inserted")
#Get database table
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)



#Fetch all Names from Employees
import mysql.connector
db_connection = mysql.connector.connect(
  host= "localhost",
  user= "root",
  passwd= "Sqlpython123#",
  database="records"
  )


db_cursor = db_connection.cursor()
db_cursor.execute("SELECT name FROM employee ")
myresult=db_cursor.fetchall()
for x in myresult:
    print(x)



