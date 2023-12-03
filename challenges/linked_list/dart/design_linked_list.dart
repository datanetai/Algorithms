/*
* @lc app=leetcode id=707 lang=dart
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

// @lc code=start
class Node {
  int? val;
  Node? next;
  Node? prev;

  Node(int val) {
    this.val = val;
    this.next = null;
    this.prev = null;
  }
}

class MyLinkedList {
  Node? head;
  int size = 0;
  MyLinkedList() {
    this.head = null;
    this.size = 0;
  }

  int get(int index) {
    if (index < 0 || index >= this.size) {
      return -1;
    }
    Node? temp = this.head;
    int i = 0;
    while (i < index && temp != null) {
      temp = temp.next;
      i++;
    }
    return temp?.val ?? -1;
  }

  void addAtHead(int val) {
    Node node = new Node(val);
    if (this.head == null) {
      this.head = node;
      this.size++;
      return;
    }
    node.next = this.head;
    this.head?.prev = node;
    this.head = node;
    this.size++;
  }

  void addAtTail(int val) {
    if (this.head == null) {
      this.addAtHead(val);
      return;
    }
    Node? temp = this.head;
    while (temp!.next != null) {
      temp = temp.next;
    }
    Node node = new Node(val);
    temp.next = node;
    node.prev = temp;
    this.size++;
  }

  void addAtIndex(int index, int val) {
    if (index < 0 || index > this.size) {
      return;
    }
    if (index == 0) {
      this.addAtHead(val);
      return;
    }
    if (index == this.size) {
      this.addAtTail(val);
      return;
    }

    Node? temp = this.head;
    int i = 0;
    while (i < index && temp != null) {
      temp = temp.next;
      i++;
    }
    Node node = new Node(val);
    node.next = temp;
    node.prev = temp?.prev;
    temp?.prev?.next = node;
    temp?.prev = node;
    this.size++;
  }

  void deleteAtIndex(int index) {
    if (index < 0 || index >= this.size) {
      return;
    }

    Node? temp = this.head;
    for (int i = 0; i < index; i++) {
      temp = temp?.next;
    }
    if (temp?.prev != null) {
      temp?.prev?.next = temp.next;
    } else {
      this.head = temp?.next;
    }
    if (temp?.next != null) {
      temp?.next?.prev = temp.prev;
    }
    this.size--;
  }

  void printAll() {
    Node? temp = this.head;
    print('size: ${this.size}');
    while (temp != null) {
      print(temp.val);
      temp = temp.next;
    }
  }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = MyLinkedList();
 * int param1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */

// @lc code=end

void main() {
  MyLinkedList obj = new MyLinkedList();
  obj.addAtHead(1);
  obj.addAtTail(3);
  obj.addAtIndex(1, 2);
  obj.printAll();
  // print(obj.get(1));
  obj.deleteAtIndex(1);
  obj.printAll();
  print("_______");
  print(obj.get(1));
}
