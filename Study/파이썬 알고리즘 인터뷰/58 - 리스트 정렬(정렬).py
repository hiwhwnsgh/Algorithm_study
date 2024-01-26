# p. 489
# 두 정렬 리스트 병합
from LinkeList import ListNode
def mergeTwoLists(l1: ListNode, l2 : ListNode) -> ListNode:
    if l1 and l2:
        if l1.val > l2.val:
            l1,l2 = l2,l1
        l1.next = mergeTwoLists(l1.next,l2)
    return l1 or l2

def sortList(head : ListNode) -> ListNode:
    if not (head and head.next):
        return head
    
    # 런너 기법 활용
    half, slow, fast = None, head, head
    while fast and fast.next:
        half, slow, fast = slow, slow.next, fast.next.next
    half.next = None

    # 분할 재귀호출
    l1 = sortList(head)
    l2 = sortList(slow)
    print(l1.val,'\n',l2.val)
    return mergeTwoLists(l1,l2)

head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
while head:
    print(head.val)
    head = head.next
head = sortList(head)
while head:
    print(head.val)
    head = head.next