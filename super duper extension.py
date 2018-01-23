#!/usr/bin/env python
# Author : Abbey Pates
# Date : 23.01.18
# Version : 2

# ask user for a value and check their reply - if not a number the loop is restarted
# checks value is in parameters 
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


def fibbonachiSequence (firstValue, secondValue, numberResults):
   resultStr = str(firstValue) + ", " + str(secondValue)
   lastValue = secondValue
   penultimateValue = firstValue
   
   for counter in range(2, numberResults):
      nextValue = lastValue + penultimateValue
      resultStr = resultStr + ", " + str(nextValue)
      penultimateValue = lastValue
      lastValue = nextValue
      
   print(resultStr)

if __name__ == '__main__':
   print "Fibbonachi Sequence"
   print "==================="


firstValue = askUser("Please select the first value in your fibbonachi sequence ", 0, 5000000000)
secondValue = askUser("Please select the second value in your fibbonachi sequence ", firstValue, 5000000000)
numberResults = askUser("How many results?", 2, 5000000000)

fibbonachiSequence (firstValue, secondValue, numberResults)
      
