#CB 15/03/2019
#GMIT Data Analytics Programming & Scripting Module 2019
#Problem Sets
#Problem Set 5

#Creating a variable 'posint' to store the value being calculated and output, and asking the user to input a positive integer
posint = int (input("Please enter a positive integer: "))
#Setting up a check to ensure the number entered is a positive integer. If not, the program will return an error to the user
assert (posint > 0), 'Number must be a positive integer'

