try:
    num1, num2 = eval(input("enter 2 numbers, separated by a comma"))
    result = num1 / num2
    print("result is", result)
except ZeroDivisionError:
    print("division by zero is error !!")
except SyntaxError:
    print("comma is missing enter the numbers separatedby a comma like this: 1, 2")
except:
    print("wrong input")
else:
    print("no exceptions")
finally:
    print("this will execute no matter what")

