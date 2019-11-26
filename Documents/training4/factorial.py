import math

factorial = 1

num = int(input("please enter number you require factorial of: "))

if num < 0:
      print("sorry you can't use that number")

elif num == 0:
      print ("the factorise of 0 is 1")
else:
      for i in range (1,num + 1):
            factorial = factorial *i
      print ("The factorial of" ,num, "is", factorial)
      





