/*
 * @lc app=leetcode id=19 lang=golang
 *
 * [19] Remove Nth Node From End of List
 *
 * https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
 *
 * algorithms
 * Medium (42.96%)
 * Likes:    17522
 * Dislikes: 728
 * Total Accepted:    2.3M
 * Total Submissions: 5.4M
 * Testcase Example:  '[1,2,3,4,5]\n2'
 *
 * Given the head of a linked list, remove the n^th node from the end of the
 * list and return its head.
 *
 *
 * Example 1:
 *
 *
 * Input: head = [1,2,3,4,5], n = 2
 * Output: [1,2,3,5]
 *
 *
 * Example 2:
 *
 *
 * Input: head = [1], n = 1
 * Output: []
 *
 *
 * Example 3:
 *
 *
 * Input: head = [1,2], n = 1
 * Output: [1]
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in the list is sz.
 * 1 <= sz <= 30
 * 0 <= Node.val <= 100
 * 1 <= n <= sz
 *
 *
 *
 * Follow up: Could you do this in one pass?
 *
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
// func removeNthFromEnd(head *ListNode, n int) *ListNode {
// 	size := 0
// 	a := head
// 	for a != nil {
// 		a = a.Next
// 		size++
// 	}
// 	m := (size - n - 1)
// 	if m < 0 {
// 		return head.Next
// 	}
// 	a = head
// 	for i := 0; i < m; i++ {
// 		a = a.Next
// 	}
// 	a.Next = a.Next.Next
// 	return head
// }

// approach 2 using two pointer
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	slow := head
	fast := head
	for i := 0; i < n; i++ {
		fast = fast.Next
	}
	if fast == nil {
		return head.Next
	}

	for fast.Next != nil {
		fast = fast.Next
		slow = slow.Next
	}
	slow.Next = slow.Next.Next
	return head
}

// @lc code=end

