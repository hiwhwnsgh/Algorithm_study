array = []
for i in range(100):
    nums = []
    for j in range(86):
        nums.append(j)
    array.append(nums)
        
for i in range(len(array)):
    print(array[i])

    array.append([i for i in range(86)])