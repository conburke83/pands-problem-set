#CB 15/03/2019
#GMIT Data Analytics Programming & Scripting Module 2019
#Problem Sets
#Problem Set 3

#Reference https://www.tutorialspoint.com/python3/nested_if_statements_in_python.htm

#Setting up a controlling loop for variable 'num' for the range 1000 to 10000
for num in range (1000,10000):
    #If statement, asking if num divisible by 6
    if num % 6 == 0:
        #Nested-If statement asking is num not divisible by 12
         if num % 12 != 0:
            #If both conditions are satisified, print num, before looping to the next integer in the range
            print (num)
            #Even if both conditions are satisfied, continue to the next integer in the range
            continue