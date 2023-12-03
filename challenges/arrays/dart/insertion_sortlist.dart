/**
 * Definition for singly-linked list.
 * class ListNode {
 *   int val;
 *   ListNode? next;
 *   ListNode([this.val = 0, this.next]);
 * }
 */
class Solution {
    // Approach 1: Sort array and set the values in linked list O(nlogn)    
  ListNode? insertionSortList(ListNode? head) {
        List<int> nums = [];
            ListNode? temp = head;
            while (temp != null) {
                nums.add(temp.val);
                temp = temp.next;
            }
            nums.sort();
            temp = head;
            int i = 0;
            while (temp != null) {
                temp.val = nums[i++];
                temp = temp.next;
            }
            return head;
  }
   // Approach 2: Insertion Sort O(n^2)
    ListNode? insertionSortList(ListNode? head) {
 if (head == null) {
      return head;
    }
      ListNode? dummy = ListNode(0);
        ListNode? curr = head;
        ListNode? next = null;
        while(curr !=null ){
             next = curr.next;
             ListNode? prev = dummy;
                while(prev!.next != null && prev.next!.val < curr.val){
                    prev = prev.next;
                }
                curr.next = prev.next;
                prev.next = curr;
                curr = next;
            
        }
        return dummy.next;

}