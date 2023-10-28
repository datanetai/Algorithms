// linked list implementation
package main

type Node struct {
	data int
	next *Node
}

type LinkedList struct {
	head *Node
}

func (l *LinkedList) search(key int) *Node {
	x := l.head
	for x != nil && x.data != key {
		x = x.next
	}
	return x
}

func (l *LinkedList) insert(key int) {
	x := new(Node)
	x.data = key
	x.next = l.head
	l.head = x
}

func (l *LinkedList) insertEnd(key int) {
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

func (l *LinkedList) delete(key int) {
	head := l.head
	if head == nil {
		return
	}
	if head.data == key {
		head = head.next
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

func (l *LinkedList) print() {
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

func main() {
	l := new(LinkedList)
	l.insert(1)
	l.insert(2)
	l.insert(3)
	l.insert(4)
	l.insert(5)
	l.print()
	l.insertEnd(6)
	l.print()
	l.delete(6)
	l.print()
	l.delete(1)
	l.print()
	l.delete(3)
	l.print()
	{
		println("Doubly linked list")
		dl := new(DoublyLinkedList)
		dl.insert(1)
		dl.insert(2)
		dl.insert(3)
		dl.insert(4)
		dl.insert(5)
		dl.print()
		dl.insertEnd(6)
		dl.print()
		dl.delete(6)
		dl.print()
		dl.delete(1)
		dl.print()
		dl.delete(3)
		dl.print()
	}
}
