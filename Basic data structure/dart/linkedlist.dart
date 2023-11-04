class Node {
  int? data;
  Node? next;

  Node(int data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  Node? head;

  LinkedList() {
    this.head = null;
  }

  Node? search(int key) {
    Node? temp = this.head;
    while (temp != null) {
      if (temp.data == key) {
        return temp;
      }
      temp = temp.next;
    }
    return null;
  }

  void insert(int key) {
    Node node = Node(key);
    node.next = this.head;
    this.head = node;
  }

  void insertEnd(int key) {
    Node node = Node(key);
    if (this.head == null) {
      this.head = node;
      return;
    }
    Node? temp = this.head;
    while (temp?.next != null) {
      temp = temp?.next;
    }
    temp!.next = node;
  }

  void printList() {
    Node? temp = this.head;
    while (temp != null) {
      print(temp.data);
      temp = temp.next;
    }
  }

  void delete(int key) {
    Node? temp = this.head;
    if (temp == null) {
      print("List is empty");
      return;
    }
    if (temp.data == key) {
      this.head = temp.next;
      return;
    }
    while (temp?.next != null && temp!.next!.data != key) {
      temp = temp.next;
    }
    if (temp?.next == null) {
      print("Key not found");
      return;
    }
    temp!.next = temp.next!.next;
  }
}

class DNode{
    int? data;
    DNode? next;
    DNode? prev;
    DNode(int data){
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

class DoublyLinkedList{
    DNode? head;
    DNode? tail;
    DoublyLinkedList(){
        this.head = null;
        this.tail = null;
    }
    DNode? search(int key){
        DNode? temp = this.head;
        while(temp != null){
            if(temp.data == key){
                return temp;
            }
            temp = temp.next;
        }
        return null;
    }
   void insert(int key){
    DNode node = DNode(key);
    node.next = this.head;
    if(this.head != null){
        this.head!.prev = node;
    } else {
        this.tail = node;  // Add this line
    }
    this.head = node;
}
    void insertEnd(int key){
        DNode node = DNode(key);
        if(this.head == null && this.tail == null){
            this.head = node;
            this.tail = node;
            return;
        }
        this.tail!.next = node;
        node.prev = this.tail;
        this.tail = node;
    }
    
    void printList(){
        DNode? temp = this.head;
        while(temp != null){
            print(temp.data);
            temp = temp.next;
        }
    }

    void delete(int key){
        DNode? temp = this.head;
        if(temp == null){
            print("List is empty");
            return;
        }
        if(temp.data == key){
            this.head = temp.next;
            if(this.head != null){
                this.head!.prev = null;
            }
            return;
        }
        while(temp?.next != null && temp!.next!.data != key){
            temp = temp.next;
        }
        if(temp?.next == null){
            print("Key not found");
            return;
        }
        
        temp!.next = temp.next!.next;
        if(temp.next != null){
            temp.next!.prev = temp;
        }
    }
}

void main() {
    DoublyLinkedList list = DoublyLinkedList();
    list.insert(1);
    list.insert(2);
    list.insert(3);
    list.insertEnd(4);
    list.insertEnd(5);
    list.delete(3);
    list.printList();

}
