# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def deleteDuplicates(head: ListNode) -> ListNode:
    if not head:
        return head
    prev = head
    cur = prev.next
    while cur:
        if prev.val == cur.val:
            prev.next = cur.next
            cur = prev.next
        else:
            prev = cur
            cur = cur.next
    return head

# test
a = ListNode(1)
a.next = ListNode(1)
a.next.next = ListNode(2)
a.next.next.next = ListNode(3)
out = deleteDuplicates(a)
while out != None:
    print(out.val)
    out = out.next
        