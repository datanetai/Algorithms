# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def middleNode(head: ListNode) -> ListNode:
    tmp = head
    count = 0
    while tmp:
        count += 1
        tmp = tmp.next
    count = count // 2
    while count:
        head = head.next
        count -= 1
    return head

# runner solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def middleNode2(head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    tmp = head
    count = 0
    while tmp:
        count += 1
        tmp = tmp.next
    if count == n:
        return head.next
    count = count - n
    tmp = head
    while count > 1:
        tmp = tmp.next
        count -= 1
    tmp.next = tmp.next.next
    return head

# solution 2
# Time Complexity: O(n)
# Space Complexity: O(1)
def removeNthFromEnd2(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = dummy
    for i in range(n + 1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next
        
lst = [1,2,3,4,5,6,7,8,9,10]
head = ListNode(lst[0])
tmp = head
for i in range(1,len(lst)):
    tmp.next = ListNode(lst[i])
    tmp = tmp.next
print(middleNode2(head).val)
