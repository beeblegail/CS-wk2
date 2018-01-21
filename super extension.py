# Author: Abbey Pates 
# Date: 21/01/2018
# Title: Week 2 Prep - Super Extension
# Version 1.0
import re

x_loop = raw_input('please input the letter x')
if not re.match("^[x]*$", x_loop):
    print "Error! Only letter x allowed!"
   
def askUser(question , lowerLimit, upperLimit):
   while True:
      try:
         answer = int(raw_input(question))
      except ValueError:
         print("Not an integer value...")
         continue
      else:
         if (answer < lowerLimit) | (answer > upperLimit):
            print("Not within the range " + str(lowerLimit) + " and " + str(upperLimit))
         else:
            return (answer)
            break



counter = 0

while counter < results:
    print( counter+1, ': ', start_number+increase*counter )
    counter += 1

print('Output complete!')

start_number = askUser ("Please enter the start number:",1 ,100)
increase = askUser("Please enter the increase you would like:",1,100)
results = askUser ("Please enter the number of results you would like:",1,100)
