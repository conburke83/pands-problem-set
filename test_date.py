#CB 17/03/2019
#GMIT Data Analytics Programming & Scripting Module 2019
#Problem Sets
#Problem Set 8

#Importing the datetime type from the datetime module
from datetime import datetime

#Define variable 'today' as the type today from module datetime
today = datetime.today()
#Define the variable date_string. This is made up of the variable 'today' formatted as a string, and then the string construct defined in the brackets
date_string = today.strftime('%A %B #, %Y' + " at " + '%I:%M%p')
#Define the variable time_string. This is made up of the variable 'today' formatted as a string, and then the string construct defined in the brackets
day = today.day

if (3 < day < 21) or (23 < day < 31):
  day = str(day) + 'th'
else:
  suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
  day = str(day) + suffixes[day % 10]

print(f"{date_string.replace('#', day)}")

#Monday, January 10th 2019 at 1:15pm
