# Gven the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head:ListNode, val: int) -> ListNode:
    if not head:
        return head
    prev = head
    current = prev.next
    
    while current:
        if current.val == val:
            prev.next = current.next
            current = prev.next
        else:
            prev = current
            current = current.next
    return head if head.val != val else head.next

# recursive
def removeElements(head:ListNode, val: int) -> ListNode:
    if not head:
        return head
    head.next = removeElements(head.next, val)
    return head if head.val != val else head.next

elms = [2,3,5,3,5,4,3,3]
val = 3
lst = ListNode(elms[0])
current = lst
for i in range(1,len(elms)):
    current.next = ListNode(elms[i])
    current = current.next


result = removeElements(lst,val)
while result:
    print(result.val, end=' ')
    result = result.next
print()
# Output:
