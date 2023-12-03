/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
// floyd's cycle detection algorithm
package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	slow := head
	fast := head
	for fast != nil && fast.Next != nil {
		slow = (*slow).Next
		fast = (*fast).Next.Next
		fmt.Println(slow.Val, fast.Val)

		if slow == fast {
			return true
		}
	}
	return false
}

// using hash map
func hasCycle2(head *ListNode) bool {
	m := make(map[*ListNode]bool)
	for head != nil {
		if m[head] {
			return true
		}
		m[head] = true
		head = head.Next
	}
	return false
}

// Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

// There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

// Do not modify the linked list.

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
// floyd's cycle detection algorithm see proof below
func detectCycle(head *ListNode) *ListNode {
	slow := head
	fast := head
	for fast != nil && fast.Next != nil {
		slow = (*slow).Next
		fast = (*fast).Next.Next

		if slow == fast {
			temp := head
			for temp != slow {
				temp = temp.Next
				slow = slow.Next
			}
			return temp
		}
	}
	return nil
}

// 1. We have a linked list that may or may not have a cycle. A cycle means that some node in the list points to a previous node, forming a loop. For example, the following list has a cycle:

// 2. We want to find the node where the cycle begins, if it exists. In the above example, the node where the cycle begins is 4.

// 3. To do this, we use two pointers, one slow and one fast. The slow pointer moves one node at a time, while the fast pointer moves two nodes at a time.

// 4. We start both pointers at the head of the list and move them until they either meet or reach the end of the list. If they reach the end of the list, then there is no cycle and we return null. If they meet, then there is a cycle and we proceed to the next step.

// 5. Let's assume that the two pointers meet at some node in the cycle. We can label the distances from the head of the list to the node where the cycle begins as x, from the node where the cycle begins to the node where the pointers meet as y, and from the node where the pointers meet to the node where the cycle begins as z, as shown in the image.

// 6. The intuition behind this part of the algorithm is that **x = z**. This means that the distance from the head of the list to the node where the cycle begins is equal to the distance from the node where the pointers meet to the node where the cycle begins.

// 7. Why is this true? This is because the slow and fast pointers have traveled the same distance modulo the length of the cycle. Modulo means the remainder after dividing by a number. The length of the cycle is b + c, where b is y and c is z.

// 8. Let's see how this works mathematically. The distance traveled by the slow pointer is x + y. The distance traveled by the fast pointer is x + y + z + y, because it has to go around the cycle once more before meeting the slow pointer. The speed of the slow pointer is 1, while the speed of the fast pointer is 2, because it moves twice as fast.

// 9. We can write the equation for the time taken by both pointers as:

// $$\frac{x + y}{1} = \frac{x + y + z + y}{2}$$

// 10. Simplifying this equation, we get:

// $$2x + 2y = x + 2y + z$$

// 11. Subtracting 2y from both sides, we get:

// $$x = z$$

// 12. This proves that the distance from the head of the list to the node where the cycle begins is equal to the distance from the node where the pointers meet to the node where the cycle begins.

// 13. Therefore, by moving the start and slow pointers at the same speed, they will eventually reach the node where the cycle begins. This is because they will both cover the same distance x before reaching the node where the cycle begins.

// 14. To do this, we reset the fast pointer to the head of the list and move both pointers one node at a time until they meet. The node where they meet is the node where the cycle begins. We return this node as the answer.
