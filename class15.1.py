numbers1 = [1, 5, 7]
numbers2 = [4, 2, 9]
result = map(lambda x, y: x + y, numbers1, numbers2)
print("adittion of 2 lists")
print(list(result))
nums = [1, 3, 7, 9, 6]
def sq(n):
    return n*n
square = list(map(sq, nums))
print("square of numbers in list")
print(square)
