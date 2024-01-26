from typing import List


class ListNode:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self,head : ListNode) -> ListNode: # 연결리스트 뒤집기
        node , prev = head,None
        
        while node:
            next,node.next = node.next, prev
            prev,node = node,next
        return prev
    def toList(self,node : ListNode) -> List:   # 연결리스트를 파이썬리스트로 변환
        list : List = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    def toReversedLinkedList(self, result : str) -> ListNode: # 파이썬 리스트를 연결리스트로 변경
        prev : ListNode = None
        
        for r in result:
            node = ListNode(r)
            node.next= prev
            prev = node

        return node
    