#CB 23/03/2019
#GMIT Data Analytics Programming & Scripting Module 2019
#Problem Sets
#Problem Set 7

#Reference https://www.tutorialspoint.com/python/python_numbers.htm
#Reference https://www.geeksforgeeks.org/abs-in-python/
#Reference https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
#Reference https://www.google.com/search?q=-%3D+pytho&rlz=1C1GCEA_enIE833IE833&oq=-%3D+pytho&aqs=chrome..69i57.2568j0j7&sourceid=chrome&ie=UTF-8
#Reference https://web.microsoftstream.com/video/dca7ddaa-9512-4810-a758-237921e6440e


#Creating a user input variable 'posfpn' which is a floating point number, and which stores the value for which the user requires the square root.
posfpn = float(input("Please enter a positive floating point number: "))
#Setting up a check to ensure the number entered is a positive floating point number. If not, the program will return an error to the user.
assert (posfpn > 0), 'Number must be a positive floating point number'
#Creating a variable 'estimate' which will always have an initial value of 6. This value will be used in the below loop calculation to store the estimated square-root as it passes through the loop.
estimate = 6
#Setting up a while loop based on Go's logic for calculating a square root. The loop will run until the calculation of the square root using the 'estimate' variable gives a result that is within 0.1 of the user input variable 'posfpn'
while abs((estimate*estimate)-posfpn)>0.1:
    estimate -= ((estimate*estimate)-posfpn)/(2*estimate)
#Once the above loop is completed, print the estimated square-root within the following sentence, formatting the 'estimate' as a string and rounding it to 2 decimal places.
print(f"The square root of {posfpn} is approx. {estimate:.2f}.")