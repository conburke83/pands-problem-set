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
my_date = date.today()
calendar.day_name[my_date.weekday()]
#Setting up a variable 't', which stores the value for today's string name
t = date.today()
tday = calendar.day_name[t.weekday()]
#Setting up a variable 't-days' which stores a tuple of weekdays beginning with letter t
tdays = {"Tuesday","Friday"}

print ("Does today's day begin with a 'T'?")
if tday in tdays:
    print ("Yes - today begins with a T.")
Else: print ("No - today does not begin with a T")

