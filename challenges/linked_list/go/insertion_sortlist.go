package main

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func insertionSortList(head *ListNode) *ListNode {
	if head == nil {
		return head
	}

	dummy := &ListNode{}
	curr := head
	var next *ListNode
	var prev *ListNode = dummy
	for curr != nil {
		next = curr.Next
		if prev.Val > curr.Val {
			prev = dummy
		}

		for prev.Next != nil && prev.Next.Val < curr.Val {
			prev = prev.Next
		}

		curr.Next, prev.Next, curr = prev.Next, curr, next

	}

	return dummy.Next
}

func main() {
	lst := &ListNode{Val: 4, Next: &ListNode{Val: 2, Next: &ListNode{Val: 1, Next: &ListNode{Val: 3}}}}
	insertionSortList(lst)
	// print
	for lst != nil {
		println(lst.Val)
		lst = lst.Next
	}
}
