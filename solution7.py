#CB 23/03/2019
#GMIT Data Analytics Programming & Scripting Module 2019
#Problem Sets
#Problem Set 7

#Importing the datetime and calendar modules

#Creating a variable 'posfpn' to store the value being calculated and output, and asking the user to input a positive integer.
posfpn = float(input("Please enter a positive floating point number: "))
#Setting up a check to ensure the number entered is a positive integer. If not, the program will return an error to the user.
assert (posfpn > 0), 'Number must be a positive'
estimate = 6
while abs ((estimate*estimate)-posfpn)>0.1:
    estimate -= ((estimate*estimate)-posfpn)(2*estimate)
print (f"The square root of {posfpn} is approx. {estimate}.")