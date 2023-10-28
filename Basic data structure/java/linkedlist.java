class Main {
    public static void main(String[] args) {
        SinglyLinkedList list = new SinglyLinkedList();
        list.insert(10);
        list.insert(20);
        list.insert(30);
        list.insertAfter(40);
        list.print();
        list.delete(20);
        list.print();
        DoubleLinkedList list2 = new DoubleLinkedList();
        list2.insert(10);
        list2.insert(20);
        list2.insert(30);
        list2.insertAfter(40);
        list2.print();
        list2.delete(20);
        list2.print();

    }
}

class Node {
    int data;
    Node next;
    Node prev;

    public Node(int data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }

}

// singly linked list
public class SinglyLinkedList {
    Node head;

    public SinglyLinkedList() {
        this.head = null;
    }

    public Node search(int n) {
        Node x = head;
        while (x != null && x.data != n) {
            x = x.next;
        }
        if (x == null) {
            return null;
        }
        return x;
    }

    public void insert(int n) {
        Node x = new Node(n);
        x.next = head;
        head = x;
    }

    // insert at the end
    public void insertAfter(int n) {
        Node x = new Node(n);
        if (head == null) {
            head = x;
            return;
        }
        Node y = head;
        while (y.next != null) {
            y = y.next;
        }
        y.next = x;
    }

    public void delete(int n) {
        if (head == null) {
            return;
        }
        if (head.data == n) {
            head = head.next;
            return;
        }
        Node x = head;
        while (x.next != null && x.next.data != n) {
            x = x.next;
        }
        if (x.next == null) {
            return;
        }
        x.next = x.next.next;
    }

    public void print() {
        Node x = head;
        while (x != null) {
            System.out.printf("%d ", x.data);
            x = x.next;
        }
        System.out.println();
    }

}

class DoubleLinkedList {
    Node head;

    public DoubleLinkedList() {
        this.head = null;
    }

    public Node search(int n) {
        Node x = head;
        while (x != null && x.data != n) {
            x = x.next;
        }
        if (x == null) {
            return null;
        }
        return x;
    }

    public void insert(int n) {
        Node x = new Node(n);
        x.next = head;
        if (head != null) {
            head.prev = x;
        }
        head = x;
    }

    public void insertAfter(int n) {
        Node x = new Node(n);
        if (head == null) {
            head = x;
            return;
        }
        Node y = head;
        while (y.next != null) {
            y = y.next;
        }
        y.next = x;
        x.prev = y;
    }

    public void delete(int n) {
        if (head == null) {
            return;
        }
        if (head.data == n) {
            head = head.next;
            return;
        }
        Node x = head;
        while (x.next != null && x.next.data != n) {
            x = x.next;
        }
        if (x.next == null) {
            return;
        }
        x.next = x.next.next;
        if (x.next != null) {
            x.next.prev = x;
        }
    }

    public void print() {
        Node x = head;
        while (x != null) {
            System.out.printf("%d ", x.data);
            x = x.next;
        }
        System.out.println();
    }
}