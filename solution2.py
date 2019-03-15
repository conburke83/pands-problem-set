#CB 03/03/2019
#GMIT Data Analytics Programming & Scripting Module 2019
#Problem Sets
#Problem Set 2

#Reference https://stackoverflow.com/questions/8380389/how-to-get-day-name-in-datetime-in-python
#Reference https://pythontic.com/datetime/date/weekday
#Reference https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date-in-python

#Importing the datetime and calendar modules
from datetime import date
import calendar
#Setting up a variable 't', which stores the value for todays date
t = date.today()
#Setting up a variable 'tday', which stores the value for todays day
tday = calendar.day_name[t.weekday()]
#Setting up a variable which always converts the tday string to all-lowercase, to avoid uppercase/lowercase ambigouity when looking up in the tupple
tdaylower = tday.lower()
#Setting up a variable 't-days' which stores a tuple of weekdays beginning with the letter 't'
tdays = {"tuesday","thursday"}
#Always print the following question first, to give context in the output
print ("Does today's day begin with a 'T'?")
#Lookup todays day, stored in varaiable 'tdaylower', in the tupple 'tdays'
if tdaylower in tdays:
    #If true (in the tupple), print this statement
    print ("Yes - today begins with a T.")
    #If false (not in the tupple), print this statement
else:
    print ("No - today does not begin with a T")

