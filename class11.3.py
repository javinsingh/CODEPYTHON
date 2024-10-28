L = [4, 5, 1, 2, 9, 7, 10, 8]
print("original list:",L)
count = 0
for i in L:
    count += i
avg = count/len(L)
print("sum =",count) 
print("avarege =",avg)
L.sort()
print("smallest element is:",L[0])
print("largest element is:",L[-1])
