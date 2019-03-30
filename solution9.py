#CB 30/03/2019
#GMIT Data Analytics Programming & Scripting Module 2019
#Problem Sets
#Problem Set 9

#Reference https://www.bbc.com/news/entertainment-arts-47740423
#Reference https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
#Reference https://stackoverflow.com/questions/38744244/glob-error-io-textiowrapper-name-mode-r-encoding-cp1252-reading-tex

#Creating a user input variable 'userfile', in which the user will enter the name of the user file they would like the program to operate on
userfile = input("Please enter the name of a txt file: ")

#Open the text file 'solution9_text in read mode and give it the object name 'f'.
#Opening via a 'with' statement to perform actions on the file, and also to close the txt file automatically at the end of the 'with' statement
with open(userfile,'r') as f:
        lineslist = list(f)[1::2]
        print (lineslist)

