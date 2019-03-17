#CB 17/03/2019
#GMIT Data Analytics Programming & Scripting Module 2019
#Problem Sets
#Problem Set 6

#Reference https://teamtreehouse.com/community/trying-to-take-out-every-other-item-in-a-list

#Creating a variable 'sentence' which asks the user to input a sentence, and then stores the input as a string.
sentence = str (input("Please enter a sentence: "))
#Creating a variable 'words' which splits the 'sentence' into a list of individual words
words = sentence.split()
#Setting up a variable 'output' to store the string output of words
output = ''
#Creating a function which considers each item in the list, starting at the first item in the list, ending at the last item in the 'words lis' and only looking at every second item after the first
for item in range(0, len(words), 2):
    #For each item returned by the above function, append it to the string variable 'output'.
    output += words[item]
    #Append a space " " after each item returned by the above function is appended it to the string variable 'output'.
    output += " "
#When the for function has reached the last item in the list and completed, print the 'output' string variable that has been created by the program.   
print(output)