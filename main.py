from pydoc import doc
import os
import homograph
#import canonicalization

"""  
Retrieves user input running them through canonicalization
and homograph functions displaying results to user.
"""
def userInputTests():
   #get user inputs to test whether they are homographs
   homoTestString1 = input("Enter First File Path: ")
   homoTestString2 = input("Enter Second File Path: ")
   #Run Individual Test
   result = runTest(homoTestString1, homoTestString2) 
   #print result to users
   if result:
      print("These Two Paths Are Homographs\n")
   else:
      print("These Two Paths Are NOT Homographs\n")

"""
Contains both the string sets and logic to run thorugh multiple
set of tests showing homographs and non-homograph sets.
These test sets are all arbitrary and don't take into account the users system.
"""
def runPremadeTestCases():
   #arbitrary working directory for proof of concept
   cwd = "\\home\\cse453\\week05\\"
   #all strings within will be homographs to strings within homographStrings list (this list should be longer than non homograph list)
   homographStrings = [f"{cwd}test.txt", f"{cwd}.\\test.txt", f"{cwd}../../../../../../home/cse453/week05/test.txt",
   f"{cwd}..\\week05\\..\\week05\\..\\week05\\test.txt", f"{cwd}..\\week04\\..\\week05\\test.txt", f"{cwd}./test.txt"]
   #all strings will not be homographs to the homographStrings list
   nonHomographStrings = ["..\\week04\\test.txt"]

   #loop through homograph tests using the length of the test cases
   for i in range(0, len(homographStrings)):
      #using i to get element 0 starting at the front of the list and length - (i + 1) to get the end of the list
      result = runTest(homographStrings[i], homographStrings[len(homographStrings)-(i+1)])
      if result:
         print("These Two Paths Are Homographs\n")
      else:
         print("These Two Paths Are NOT Homographs\n")

   #loop through non-homograph tests
   for i in range(0, len(nonHomographStrings)):
      #using i to get element 0 of both homographString and nonHomographStrings
      result = runTest(homographStrings[i], nonHomographStrings[i])
      if result:
         print("These Two Paths Are Homographs\n")
      else:
         print("These Two Paths Are NOT Homographs\n")
"""  
Test runner invoking other classes to run through canonicalization and homograph tests
"""
def runTest(homoTestString1, homoTestString2):
   #canonicalize use inputs cleansing them for homograph test
   #homoTestString1 = CANONICALIZE(homoTestString1)
   #homoTestString2 = CANONICALIZE(homoTestString2)
   #prepend CWD to strings
   homoTestString1 = os.getcwd() + homoTestString1
   homoTestString2 = os.getcwd() + homoTestString2
   #push strings to homograph function
   return homograph.test_homograph(homoTestString1, homoTestString2)

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
         runPremadeTestCases()
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

