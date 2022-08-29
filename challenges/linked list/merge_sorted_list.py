# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    if not list1:
        return list2
    if not list2:
        return list1
    
    result = None
    if list1.val < list2.val:
        result = list1
        list1 = list1.next
    else:
        result = list2
        list2 = list2.next
    
    current = result
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    if list1:
        current.next = list1
    if list2:
        current.next = list2
    return result
    
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
result = mergeTwoLists(list1, list2)
assert result.val == 1
assert result.next.val == 1
assert result.next.next.val == 2
assert result.next.next.next.val == 3
assert result.next.next.next.next.val == 4
assert result.next.next.next.next.next.val == 4
print("Passed all tests!")