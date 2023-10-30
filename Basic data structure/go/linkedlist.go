// linked list implementation
package main

type Node struct {
	data int
	next *Node
}

type LinkedList struct {
	head *Node
}

func (l *LinkedList) Search(key int) *Node {
	x := l.head
	for x != nil && x.data != key {
		x = x.next
	}
	return x
}

func (l *LinkedList) Insert(key int) {
	x := new(Node)
	x.data = key
	x.next = l.head
	l.head = x
}

func (l *LinkedList) InsertEnd(key int) {
	x := new(Node)
	x.data = key
	if l.head == nil {
		l.head = x
		return
	}
	y := l.head
	for y.next != nil {
		y = y.next
	}
	y.next = x
}

func (l *LinkedList) Delete(key int) {
	head := l.head
	if head == nil {
		return
	}
	if head.data == key {
		l.head = head.next
		return
	}
	x := head
	for x.next != nil && x.next.data != key {
		x = x.next
	}
	if x.next == nil {
		return
	}
	x.next = x.next.next
}

func (l *LinkedList) Print() {
	x := l.head
	for x != nil {
		print(x.data, " ")
		x = x.next
	}
	println()
}

type DNode struct {
	data int
	next *DNode
	prev *DNode
}
type DoublyLinkedList struct {
	head *DNode
}

func (l *DoublyLinkedList) search(key int) *DNode {
	x := l.head
	for x != nil && x.data != key {
		x = x.next
	}
	return x
}
func (l *DoublyLinkedList) insert(key int) {
	x := new(DNode)
	x.data = key
	x.next = l.head
	if l.head != nil {
		l.head.prev = x
	}
	l.head = x
	x.prev = nil
}

func (l *DoublyLinkedList) insertEnd(key int) {
	x := new(DNode)
	x.data = key
	if l.head == nil {
		l.head = x
		return
	}
	y := l.head
	for y.next != nil {
		y = y.next
	}
	y.next = x
	x.prev = y
}

func (l *DoublyLinkedList) delete(key int) {
	x := l.head
	for x != nil && x.data != key {
		x = x.next
	}
	if x == nil {
		return
	}
	if x.prev != nil {
		x.prev.next = x.next
	} else {
		l.head = x.next
	}
	if x.next != nil {
		x.next.prev = x.prev
	}
}
func (l *DoublyLinkedList) print() {
	x := l.head
	for x != nil {
		print(x.data, " ")
		x = x.next
	}
	println()
}
