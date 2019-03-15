#CB 15/03/2019
#GMIT Data Analytics Programming & Scripting Module 2019
#Problem Sets
#Problem Set 4

#Reference https://www.quora.com/How-can-I-make-sure-the-user-inputs-a-positive-integer-in-Python

#Creating a variable 'posint' to store the value being calculated and output, and asking the user to input a positive integer
posint = int (input("Please enter a positive integer: "))
#Setting up a check to ensure the number entered is a positive integer. If not, the program will return an error to the user
assert (posint > 0), 'Number must be a positive integer'

#Setting up a loop, which will run until the variable 'posint' is equal to 1
while posint != 1:
    #If statement, asking if posint is even (remainder is zero when divided by 2)
    if posint % 2 == 0:
        #If above statement is true, posint is divided by 2 and the new value for posint is printed to the screen
        posint = posint / 2
        print (posint)
    #Else If statement, asking if posint is odd (remainder is not zero when divided by 2)    
    elif posint % 2 != 0:
        #If above statement is true, posint is multiplie by 3 and 1 added, and the new value for posint is printed to the screen
        posint = (posint*3)+1
        print(posint)
    continue

