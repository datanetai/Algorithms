class Main {
    public static void main(String[] args) {
        Stack stack = new Stack(10);
        stack.push(10);
        stack.push(20);
        stack.push(30);
        try {
            for (int i = 0; i < 4; i++) {
                System.out.println(stack.pop());
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        Queue queue = new Queue(10);
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);
        try {
            for (int i = 0; i < 4; i++) {
                System.out.println(queue.dequeue());
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());

        }
    }
}

class Stack {
    private int top;
    private int[] stack;
    private int size;

    public Stack(int size) {
        this.size = size;
        this.stack = new int[size];
        this.top = -1;
    }

    public void push(int value) {
        if (this.top == this.size - 1) {
            throw new RuntimeException("Stack Overflow");

        }
        this.stack[++this.top] = value;
    }

    public int pop() {
        if (this.top == -1) {
            throw new RuntimeException("Stack Underflow");
        }
        int val = this.stack[this.top--];
        return val;
    }

    public boolean isEmpty() {
        return this.top == -1;
    }

    public int peek() {
        return this.stack[this.top];
    }
}

class Queue {
    private int size;
    private int top;
    private int bottom;
    private int[] queue;

    public Queue(int size) {
        this.queue = new int[size];
        this.top = 0;
        this.bottom = 0;
        this.size = size;
    }

    public void enqueue(int el) {
        // Check if the queue is full
        if ((this.top + 1) % this.size == this.bottom) {
            throw new RuntimeException("Queue Overflow");
        }
        this.queue[this.top] = el;
        this.top = (this.top + 1) % this.size;
    }

    public int dequeue() {
        // Check if the queue is empty
        if (this.top == this.bottom) {
            throw new RuntimeException("Queue Underflow");
        }
        int el = this.queue[this.bottom];
        this.bottom = (this.bottom + 1) % this.size;
        return el;
    }

    public boolean isEmpty() {
        return this.top == this.bottom;
    }

    public boolean isFull() {
        return (this.top + 1) % this.size == this.bottom;
    }
}
