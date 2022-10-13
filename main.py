import os
from pydoc import doc
import os
import homograph
#import canonicalization

"""  
Retrieves user input running them through canonicalization
and homograph functions displaying results to user
"""
def userInputTests():
   #get user inputs to test whether they are homographs
   homoTestString1 = input("Enter First File Path: ")
   homoTestString2 = input("Enter Second File Path: ")
   #canonicalize use inputs cleansing them for homograph test
   #homoTestString1 = CANONICALIZE(homoTestString1)
   #homoTestString2 = CANONICALIZE(homoTestString2)
   #push strings to homograph function
   result = homograph.test_homograph(homoTestString1, homoTestString2)
   #print result to users
   if result:
      print("These Two Paths Are Homographs")
   else:
      print("These Two Paths Are NOT Homographs")

"""
Contains both the string sets and logic to run thorugh multiple
set of tests showing homographs and non-homograph sets
"""
def runTestCases():
   #all strings within will be homographs to strings within homographStrings list
   homographStrings = []
   #all strings will not be homographs to the homographStrings list
   nonHomographStrings = []

   #loop through homograph tests


   #loop through non-homograph tests
   

"""  
Main logic, gets user choice for basic menu system using a loop
to ensure correct pathway choices.
"""
cwd = os.getcwd()
print(cwd)
#Show user choices
print("1 - Manual String Entry")
print("2 - Run Automatic Test Cases")
print("3 - Exit Program")

#Get User Choice | 1= user input | 2= test cases | 3= exit
while True:
   try:
      choice = int(input("Enter Choice: "))
      if choice==1:
      #pushes to user input logic
         print("Manual String Entry")
         userInputTests()
      elif choice==2:
      #pushes to automatic tests logic
         print("Running Test Cases")
         runTestCases()
      elif choice==3:
      #exits program
         print("Exiting")
         break;
      else:
      #catches invalid numbers
         print("Invalid Choice")
   #catch exceptions to int casting
   except ValueError:
      print("Invalid")
      continue

