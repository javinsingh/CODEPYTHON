s1 = {2, 5, 7}
s2 = {"d", "a", "e"}
s3 = list(zip(s1, s2))
print(s3,"\n")
list1 = [30, 50, 10, 60]
list2 = [300, 500, 100, 600]
for x, y in zip(list1, list2[::-1]):
    print(x, y)
stocks = ['apple', 'tesla', 'lunchly']
prices = [1023, 4834, 1733]
new_dict = {stocks: prices for stocks,
                     prices in zip(stocks, prices)}
print('\n{}'.format(new_dict))

