#CB 15/03/2019
#GMIT Data Analytics Programming & Scripting Module 2019
#Problem Sets
#Problem Set 5

#Creating a variable 'posint' to store the value being calculated and output, and asking the user to input a positive integer.
posint = int (input("Please enter a positive integer: "))
#Setting up a check to ensure the number entered is a positive integer. If not, the program will return an error to the user.
assert (posint > 0), 'Number must be a positive integer'
#Setting up a variable for storing the incremental value which will be the divisor of the posint value.
incvalue = 2

#Setting up a loop which will divide the user integer by all numbers up to the user integer, starting at 2.
while incvalue < posint:
    #If-statement within the loop asking if 'posint' divided by 'incvalue' leaves a remainder of zero.
    if posint % incvalue == 0:
        #If true, program will print "That is a prime number", and then break out of the loop.
        print ("That is not a prime number")
        break
    #If the first if-statement is false, program will add 1 to the 'incvalue', and then return to the start of the loop and divide the 'posint' by the next number.
    incvalue = incvalue + 1
#If the while loop completes without satisfying the first if-statement for any value of 'incvalue' the program will print "That is a prime number".
else:
    print ("That is a prime number")