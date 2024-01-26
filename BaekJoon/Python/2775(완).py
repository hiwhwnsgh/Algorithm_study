T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    array = [[1,2,3,4]]
    for j in range(k):
        array2= []
        count =0
        for z in range(n):
            count+=array[j][z]
            array2.append(count)
        array.append(array2)
    print(array[k][n-1])