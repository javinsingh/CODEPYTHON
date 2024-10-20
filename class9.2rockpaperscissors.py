import random

options = ["Rock", "Paper", "Scissors"]

user_choice = input("chosse Rock, Paper and Scissors ")

computer_choice = random.choice(options)

print("your choice:",user_choice)
print("computer choice:",computer_choice)

if user_choice == computer_choice:
    print("its a tie!")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("the Rock smashes the Scissors, you win!")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("the Scissors cuts the Paper, you win!")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("the Paper covers the Rock, u win!")
else:
    print("u lose")
