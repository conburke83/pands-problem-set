#CB 17/03/2019
#GMIT Data Analytics Programming & Scripting Module 2019
#Problem Sets
#Problem Set 8
#Output the date in the following format:
#Monday, January 10th 2019 at 1:15pm

#Importing the datetime type from the datetime module
from datetime import datetime

#Define variable 'today' as the type today from module datetime
today = datetime.today()
#Define the variable date_string. This is made up of the variable 'today' formatted as a string, and then the string construct defined in the brackets
date_string = today.strftime('%A %B #, %Y' + " at ")
#Define the variable time_string. This is made up of the variable 'today' formatted as a string, and then the string construct defined in the brackets. This also converts the output to lowercase. (This is the reason for a seperate variable for the time, as I wanted to convert the AM/PM to lowercase, but not the full date string).
time_string = today.strftime('%I:%M%p').lower()

#Define the variable 'day' as the type day from the class today. This variable is to be used in the below if-statement for determining how to add the date suffix
day = today.day

#If statement for adding the suffix to the day. If the day is between 3 and 21 or between 23 and 31 append 'st' to the end of the day string.
if (3 < day < 21) or (23 < day < 31):
  day = str(day) + 'th'
#Otherwise, append the suffix per the following tupple, for days 1,2 & 3, and also if any day divided by 10 = 1,2 or 3 (This appends the suffix for the 10th, 20th and 30th)
else:
  suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
  day = str(day) + suffixes[day % 10]

#Print the output, which is a concatenation of the strings date_string and time_string. Note, the 'replace' function which swaps out the '#' and swaps in the 'day' variable which has the date suffix
print(f"{date_string.replace('#', day)}{time_string}")
