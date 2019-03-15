#CB 03/03/2019
#GMIT Data Analytics Programming & Scripting Module 2019
#Problem Sets
#Problem Set 2

#Reference https://stackoverflow.com/questions/8380389/how-to-get-day-name-in-datetime-in-python
#Reference https://pythontic.com/datetime/date/weekday

#Importing the datetime module
import datetime
#Setting up a variable 't', which stores the value for today's string name
t = datetime.datetime.now()
#Setting up a variable 'tdays' which stores a tuple of weekdays beginning with letter t
tdays = ("Tuesday","Thursday")

print ("Does today's day begin with a 'T'?")
if t[0] == "T":
    print ("Yes - today begins with a T.")
Else: print ("No - today does not begin with a T")

