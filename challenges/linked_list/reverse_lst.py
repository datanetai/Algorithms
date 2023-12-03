# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
from threading import current_thread


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  
        self.next = next
def reverseList(head: ListNode) -> ListNode:
    if head.next == None:
        return head
    else:
        new_head = reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

# iterative 
def reverseList2(head: ListNode) -> ListNode:
    prev = None
    cur = head
    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    return prev

# test
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)
a.next.next.next.next.next = ListNode(6)

rev = reverseList2(a)
while rev != None:
    print(rev.val)
    rev = rev.next

    




        
