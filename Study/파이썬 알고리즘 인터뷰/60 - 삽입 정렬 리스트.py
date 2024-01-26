from LinkeList import ListNode
def insertionSortList(head : ListNode) -> ListNode:
    # 초깃값 변경
    cur = parent = ListNode(0)
    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next
        if head and head.next and cur.next:
            print("첫번째",head.val,head.next.val,cur.next.val)
        cur.next, head.next ,head = head , cur.next, head.next
        if head and head.next and cur.next:
            print("두번째",head.val,head.next.val,cur.next.val)
        #필요한 경우에만 cur 포인터가 되돌아가도록 처리
        if head and cur.val > head.val:
            cur = parent
    return parent.next

head = ListNode(4)
head.next= ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

result = insertionSortList(head)
while result:
    #print(result.val)
    result = result.next     