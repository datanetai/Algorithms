/*
* @lc app=leetcode id=707 lang=golang
*
* [707] Design Linked List
*
* https://leetcode.com/problems/design-linked-list/description/
*
  - algorithms
  - Medium (27.97%)
  - Likes:    2474
  - Dislikes: 1550
  - Total Accepted:    293.6K
  - Total Submissions: 1M
  - Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\n' +
    '[[],[1],[3],[1,2],[1],[1],[1]]'

*
* Design your implementation of the linked list. You can choose to use a
* singly or doubly linked list.
* A node in a singly linked list should have two attributes: val and next. val
* is the value of the current node, and next is a pointer/reference to the
* next node.
* If you want to use the doubly linked list, you will need one more attribute
* prev to indicate the previous node in the linked list. Assume all nodes in
* the linked list are 0-indexed.
*
* Implement the MyLinkedList class:
*
*
* MyLinkedList() Initializes the MyLinkedList object.
* int get(int index) Get the value of the index^th node in the linked list. If
* the index is invalid, return -1.
* void addAtHead(int val) Add a node of value val before the first element of
* the linked list. After the insertion, the new node will be the first node of
* the linked list.
* void addAtTail(int val) Append a node of value val as the last element of
* the linked list.
* void addAtIndex(int index, int val) Add a node of value val before the
* index^th node in the linked list. If index equals the length of the linked
* list, the node will be appended to the end of the linked list. If index is
* greater than the length, the node will not be inserted.
* void deleteAtIndex(int index) Delete the index^th node in the linked list,
* if the index is valid.
*
*
*
* Example 1:
*
*
* Input
* ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get",
* "deleteAtIndex", "get"]
* [[], [1], [3], [1, 2], [1], [1], [1]]
* Output
* [null, null, null, null, 2, null, 3]
*
* Explanation
* MyLinkedList myLinkedList = new MyLinkedList();
* myLinkedList.addAtHead(1);
* myLinkedList.addAtTail(3);
* myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
* myLinkedList.get(1);              // return 2
* myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
* myLinkedList.get(1);              // return 3
*
*
*
* Constraints:
*
*
* 0 <= index, val <= 1000
* Please do not use the built-in LinkedList library.
* At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and
* deleteAtIndex.
*
*
*/
package main

import "fmt"

// @lc code=start

type Node struct {
	val  int
	next *Node
	prev *Node
}
type MyLinkedList struct {
	head *Node
	tail *Node
	size int
}

func Constructor() MyLinkedList {
	return MyLinkedList{size: 0} // set the size to zero
}

func (this *MyLinkedList) Get(index int) int {
	if index < 0 || index >= this.size {
		return -1
	}
	// if index is in the first half
	if index < this.size/2 {
		temp := this.head
		for i := 0; i < index; i++ {
			temp = temp.next
		}
		return temp.val
	}
	// if index is in the second half
	temp := this.tail
	for i := this.size - 1; i > index; i-- {
		temp = temp.prev
	}
	return temp.val

}

func (this *MyLinkedList) AddAtHead(val int) {
	node := &Node{val: val}
	if this.head == nil {
		this.head = node
		this.tail = node
		this.size++

		return
	}
	node.next = this.head
	this.head.prev = node
	this.head = node

	this.size++

}

func (this *MyLinkedList) AddAtTail(val int) {
	node := &Node{val: val}
	if this.head == nil {
		this.AddAtHead(val)
		return
	}
	this.tail.next = node
	node.prev = this.tail
	this.tail = node
	this.size++

}

func (this *MyLinkedList) AddAtIndex(index int, val int) {
	if index < 0 || index > this.size {
		return
	}
	if index == 0 {
		this.AddAtHead(val)
		return
	}
	if index == this.size {
		this.AddAtTail(val)
		return
	}
	var temp *Node
	if index < this.size/2 {
		temp = this.head
		for i := 0; i < index; i++ {
			temp = temp.next
		}
	} else {
		temp = this.tail
		for i := this.size - 1; i > index; i-- {
			temp = temp.prev
		}
	}
	node := &Node{val: val, next: temp, prev: temp.prev}
	temp.prev.next = node
	temp.prev = node
	this.size++
}
func (this *MyLinkedList) DeleteAtIndex(index int) {
	if index < 0 || index >= this.size {
		return
	}
	temp := this.head
	for i := 0; i < index; i++ {
		temp = temp.next
	}

	// If deleting the first node
	if temp.prev == nil {
		this.head = temp.next
	} else {
		temp.prev.next = temp.next
	}

	// If deleting the last node
	if temp.next == nil {
		this.tail = temp.prev
	} else {
		temp.next.prev = temp.prev
	}

	this.size--
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Get(index);
 * obj.AddAtHead(val);
 * obj.AddAtTail(val);
 * obj.AddAtIndex(index,val);
 * obj.DeleteAtIndex(index);
 */
// @lc code=end

func (this *MyLinkedList) printall() {
	temp := this.head
	fmt.Println("List: ")
	for temp != nil {
		fmt.Print(temp.val, " ")
		temp = temp.next
	}
	fmt.Println("Size: ", this.size)
	fmt.Println()
}
func main() {
	obj := Constructor()
	obj.AddAtHead(1)
	obj.AddAtTail(3)
	obj.printall()
	obj.AddAtIndex(1, 2)
	obj.printall()
}
