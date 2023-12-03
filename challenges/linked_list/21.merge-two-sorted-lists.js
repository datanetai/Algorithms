/*
 * @lc app=leetcode id=21 lang=javascript
 *
 * [21] Merge Two Sorted Lists
 *
 * https://leetcode.com/problems/merge-two-sorted-lists/description/
 *
 * algorithms
 * Easy (63.38%)
 * Likes:    20519
 * Dislikes: 1916
 * Total Accepted:    3.7M
 * Total Submissions: 5.8M
 * Testcase Example:  '[1,2,4]\n[1,3,4]'
 *
 * You are given the heads of two sorted linked lists list1 and list2.
 * 
 * Merge the two lists into one sorted list. The list should be made by
 * splicing together the nodes of the first two lists.
 * 
 * Return the head of the merged linked list.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: list1 = [1,2,4], list2 = [1,3,4]
 * Output: [1,1,2,3,4,4]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: list1 = [], list2 = []
 * Output: []
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: list1 = [], list2 = [0]
 * Output: [0]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in both lists is in the range [0, 50].
 * -100 <= Node.val <= 100
 * Both list1 and list2 are sorted in non-decreasing order.
 * 
 * 
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
// var mergeTwoLists = function (list1, list2) {

//     let dummy = new ListNode();
//     let tail = dummy;

//     while (list1 && list2) {
//         if (list1.val < list2.val) {
//             tail.next = list1;
//             list1 = list1.next;
//         } else {
//             tail.next = list2;
//             list2 = list2.next;
//         }
//         tail = tail.next;
//     }

//     tail.next = list1 || list2;

//     return dummy.next;
// };
// approach 2: without dummy node
var mergeTwoLists = function (list1, list2) {
    if (!list1) return list2;
    if (!list2) return list1;
    let merged;
    if (list1.val < list2.val) {
        merged = list1;
        list1 = list1.next;

    } else {
        merged = list2;
        list2 = list2.next;
    }
    let pointer = merged;
    while (list1 && list2) {
        if (list1.val < list2.val) {
            pointer.next = list1;
            list1 = list1.next;
        } else {
            pointer.next = list2;
            list2 = list2.next;
        }
        pointer = pointer.next;
    }
    pointer.next = list1 || list2;
    return merged;
};
// approach 3 recursive
var mergeTwoLists = function (list1, list2) {
    if (!list1) return list2;
    if (!list2) return list1;

    if (list1.val < list2.val) {
        list1.next = mergeTwoLists(list1.next, list2);
        return list1;
    } else {
        list2.next = mergeTwoLists(list1, list2.next);
        return list2;
    }
};
// @lc code=end

