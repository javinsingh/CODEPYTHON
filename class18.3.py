class pair_elements:
    def twosums(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target -
num], i)
            lookup[num] = i
value = int(input("enter the sum which u want to make this search"))
print("index1=%d, index2=%d" %
pair_elements().twosums((10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200), value))
