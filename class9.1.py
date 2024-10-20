import random
playing = True
number = str(random.randint(10,20))
print("i will genarate a number from 0 to 9, u have to guess what number it is one digit at the time")
while playing:
    guess = input("give me ur best guess!\n")
    if number == guess:
      print("u win the game!")
      print("the number was",number)
      break
    else:
      print("ur guess was incorrect, try again\n")