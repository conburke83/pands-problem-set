#CB 30/03/2019
#GMIT Data Analytics Programming & Scripting Module 2019
#Problem Sets
#Problem Set 10

#Creating a user input variable 'posfpn' which is a floating point number, and which stores the value for which the user requires the square root.
n = float(input("Please enter a positive floating point number: "))
#Setting up a check to ensure the number entered is a positive floating point number. If not, the program will return an error to the user.
assert (n > 0), 'Number must be a positive floating point number'

#Setting up a list called x, listing the numbers in the range to be plotted
x = (0,1,2,3,4)
x2 = [i*i for i in x]
nx = [n*i for i in x]

import matplotlib.pyplot as plotofx
import matplotlib.pyplot as plotofx2
import matplotlib.pyplot as plotofnx
plotofx.plot(x)
plotofx2.plot(x2)
plotofnx.plot(nx)
plotofx.show()
plotofx2.show()
plotofnx.show()

