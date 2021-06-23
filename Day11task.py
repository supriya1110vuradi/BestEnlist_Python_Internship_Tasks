#1. Create a python module with list and import the module in another .py file and change the value in list
list =[1,2,3,4,5,6]
import Day11task #Day11task is my module name is saved
Day11task.list1=[x+2 for x in list]
print(Day11task.list1)

#2.Install pandas package (try to import the package in a python file
#pip install pandas
import pandas as pd
import numpy as np
import sys
sys.__stdout__=sys.stdout
nos=np.array([1,2,3,4])
series1=pd.series(nos)
print(series1)

#3.Import a module that picks random number and write a program to fetch a random number from 1 to  100 on every run
import random
print("Random number is fetched:" , random.randint(1,100))

#4.Import sys package and find the python path
import sys
sys.path
print(sys.path)
