from re import I
from typing import List

class Solution:
    # 무제에 적합한 비교 함수
    @staticmethod
    def to_swap(n1 : int, n2 : int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)
    
    # 삽입 정렬 구현
    def largestNumber(self,nums : List[int]) -> str:
        i = 1
        print('초기 상태 : ',nums)
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j-1],nums[j]):
                nums[j], nums[j-1] = nums[j-1],nums[j]
                j -= 1
            i+=1
            
        return str(int(''.join(map(str,nums))))
array = [3,30,34,5,9]
ob = Solution()
result = ob.largestNumber(array)
print(result)