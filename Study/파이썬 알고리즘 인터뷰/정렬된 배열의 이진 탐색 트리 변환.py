from typing import List
from TreeNode import TreeNode
def sortedArrayToBST(nums : List[int]) -> TreeNode:
    if not nums:
        return None
    
    mid = len(nums)//2

    # 분할 정복으로 이진 검색 결과 트리 구성
    node = TreeNode(nums[mid])
    node.left = sortedArrayToBST(nums[:mid])
    node.right = sortedArrayToBST(nums[mid+1:])
    return node
root = sortedArrayToBST([-10,-7,-3,0,5,7,9])
