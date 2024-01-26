from typing import List
def merge(intervals : List[List[int]])->List[List[int]]:
    merged = []
    for i in sorted(intervals, key=lambda x: x[0]):
        print(i,merged)
        if merged and i[0] <= merged[-1][1]:
            print(merged[-1][1])
            merged[-1][1] = max(merged[-1][1],i[1])
        else:
            merged += i,
    return merged
array = [[1,3],[2,6],[8,10],[15,18]]

result = merge(array)
print(result)