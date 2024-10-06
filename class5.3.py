def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def multiplication(p,q):
    return p*q
def division(p,q):
    return p/q
print("select an operation")
print("a: addition")
print("b: subtraction")
print("c: multiplication")
print("d: division")
choice = input("enter ur choice")
num1 = int(input("enter first number"))
num2 = int(input("enter the second number"))
if choice == 'a':
   print(num1,"+",num2,"=",add(num1, num2))
elif choice == 'b':
     print(num1,"-",num2,"=",subtract(num1, num2))
elif choice == 'c':
     print(num1,"x",num2,"=",multiplication(num1, num2))
elif choice == 'd':
     print(num1,"/",num2,"=",division(num1, num2))
else:
    print("error")