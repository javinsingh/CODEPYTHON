import random
import time
number=random.randit(1,100)
def intro():
  print("may i ask for ur name")
  global name
  name = input()
  print(name + "we are going to play a game. im thinking of a number between 1-100, can u guess it?")
  if(number%2==0):
    x ='Even'
  else:
    x='odd'
  print("\n this is an {} number".format(x))
  time.sleep(.5)
  print("go ahead and guess!")
  def pick():
    
