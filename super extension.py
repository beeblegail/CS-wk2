# Author: Abbey Pates 
# Date: 21/01/2018
# Title: Week 2 Prep - Super Extension
# Version 1.0X

def askUser(question):
   while True:
      try:
         answerRaw = raw_input(question)
         answer = int(answerRaw)
      except ValueError:
         if answerRaw == 'X' :
            exit() 
         else:
            print("Not an integer value...")
         continue
      else:
         return (answer)
         break
        
def displayResults(start_number, increase, results):
   counter = 0
   while counter < results:
      print( counter+1, ': ', start_number+increase*counter )
      counter += 1
   print('Output complete!')
      

if __name__ == '__main__':
   while True:
      print "\nAnswer with X to exit:"
      start_number = askUser ("Please enter the start number:")
      increase = askUser("Please enter the increase you would like:")
      results = askUser ("Please enter the number of results you would like:")
      displayResults(start_number, increase, results)




