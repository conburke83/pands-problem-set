#CB 03/03/2019
#GMIT Data Analytics Programming & Scripting Module 2019
#Problem Sets
#Problem Set 1

#Setting up a user-defined variable 'i', and asking the user to enter a positive integer as 'i'
i = int(input("Please enter a positive integer:  "))
#Setting up the 'total' variable, which will track the output value in the while-loop
total = 0
#Setting up the while loop that will accumulate the 'total' to be output
while i > 0
    total = total + i
    i = i - 1
#print the final output for the user to see
print (total)