try:
    number = int(input("enter a number"))
    print("the number u entered is", number)
except ValueError as ex:
    print("exception:", ex)
