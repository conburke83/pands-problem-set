#CB 30/03/2019
#GMIT Data Analytics Programming & Scripting Module 2019
#Problem Sets
#Problem Set 10

#Reference https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html

#Creating a user input variable 'n' which is a floating point number, and which stores the value to e used in the function n to the power of x.
n = float(input("Please enter a positive floating point number: "))
#Setting up a check to ensure the number entered is a positive floating point number. If not, the program will return an error to the user.
assert (n > 0), 'Number must be a positive floating point number'

#Setting up a list called 'x', listing the numbers in the range to be plotted in a visual graph
x = (0,1,2,3,4)
#Setting up a list called 'x2', which lists the results of i*i from the list 'x', which will be plotted in a visual graph
x2 = [i*i for i in x]
#Setting up a list called 'nx', which lists the results of 'n' to the power of items in list 'x' from the list 'x', which will be plotted in a visual graph
nx = [n*i for i in x]

#Importing the pyplot function from the matplotlib module and assigning to a variable for each required function
import matplotlib.pyplot as plotofx
import matplotlib.pyplot as plotofx2
import matplotlib.pyplot as plotofnx

#For each matplotlib.pyplot variable, creating a plot of the function, and defining a label for each function
plotofx.plot(x, label = 'x')
plotofx2.plot(x2, label = 'x2')
plotofnx.plot(nx, label = 'nx')

#In the plot visual, printing a legend for each function being the label defined in the plot
plotofx.legend()
plotofx2.legend()
plotofnx.legend()

#For each matplotlib.pyplot plot, displaying the output in a visual
plotofx.show()
plotofx2.show()
plotofnx.show()