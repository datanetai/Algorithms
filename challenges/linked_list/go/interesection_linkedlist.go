// 160. Intersection of Two Linked Lists
// Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

// For example, the following two linked lists begin to intersect at node c1:
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *ListNode) *ListNode {
	if headA == nil || headB == nil {
		return nil
	}
	a := headA
	b := headB
	sizeA := 0
	sizeB := 0
	for a != nil {
		sizeA++
		a = a.Next
	}
	for b != nil {
		sizeB++
		b = b.Next
	}
	if a != b {
		return nil
	}
	a = headA
	b = headB

	if sizeA > sizeB {
		for i := 0; i < sizeA-sizeB; i++ {
			a = a.Next
		}
	} else {
		for i := 0; i < sizeB-sizeA; i++ {
			b = b.Next
		}
	}
	for a != b {
		a = a.Next
		b = b.Next
	}
	return a
}

// solution 2 using hash map
func getIntersectionNode2(headA, headB *ListNode) *ListNode {
	m := make(map[*ListNode]bool)
	for headA != nil {
		m[headA] = true
		headA = headA.Next
	}
	for headB != nil {
		if m[headB] {
			return headB
		}
		headB = headB.Next
	}
	return nil
}

// approach 3 two pointers see https://leetcode.com/problems/intersection-of-two-linked-lists/solutions/49785/java-solution-without-knowing-the-difference-in-len/
func getIntersectionNode3(headA, headB *ListNode) *ListNode {
	a := headA
	b := headB
	for a != b {
		if a == nil {
			a = headB
		} else {
			a = a.Next
		}
		if b == nil {
			b = headA
		} else {
			b = b.Next
		}
	}
	return a
}