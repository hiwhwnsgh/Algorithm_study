from typing import *
from LinkeList import *
head = Solution()
array = head.toReversedLinkedList([1,2,3,4,5])
head = head.reverseList(array)
odd = head
even = head.next
even_head = head.next

while even and even.next:
    odd.next,even.next = odd.next.next,even.next.next
    odd, even = odd.next, even.next
odd.next = even_head
while head:
    print(head.val)
    head = head.next
