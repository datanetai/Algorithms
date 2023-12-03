/*
 * @lc app=leetcode id=622 lang=golang
 *
 * [622] Design Circular Queue
 *
 * https://leetcode.com/problems/design-circular-queue/description/
 *
 * algorithms
 * Medium (51.32%)
 * Likes:    3389
 * Dislikes: 263
 * Total Accepted:    290.5K
 * Total Submissions: 565.8K
 * Testcase Example:  '["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]\n' +
  '[[3],[1],[2],[3],[4],[],[],[],[4],[]]'
 *
 * Design your implementation of the circular queue. The circular queue is a
 * linear data structure in which the operations are performed based on FIFO
 * (First In First Out) principle, and the last position is connected back to
 * the first position to make a circle. It is also called "Ring Buffer".
 *
 * One of the benefits of the circular queue is that we can make use of the
 * spaces in front of the queue. In a normal queue, once the queue becomes
 * full, we cannot insert the next element even if there is a space in front of
 * the queue. But using the circular queue, we can use the space to store new
 * values.
 *
 * Implement the MyCircularQueue class:
 *
 *
 * MyCircularQueue(k) Initializes the object with the size of the queue to be
 * k.
 * int Front() Gets the front item from the queue. If the queue is empty,
 * return -1.
 * int Rear() Gets the last item from the queue. If the queue is empty, return
 * -1.
 * boolean enQueue(int value) Inserts an element into the circular queue.
 * Return true if the operation is successful.
 * boolean deQueue() Deletes an element from the circular queue. Return true if
 * the operation is successful.
 * boolean isEmpty() Checks whether the circular queue is empty or not.
 * boolean isFull() Checks whether the circular queue is full or not.
 *
 *
 * You must solve the problem without using the built-in queue data structure
 * in your programming language.
 *
 *
 * Example 1:
 *
 *
 * Input
 * ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear",
 * "isFull", "deQueue", "enQueue", "Rear"]
 * [[3], [1], [2], [3], [4], [], [], [], [4], []]
 * Output
 * [null, true, true, true, false, 3, true, true, true, 4]
 *
 * Explanation
 * MyCircularQueue myCircularQueue = new MyCircularQueue(3);
 * myCircularQueue.enQueue(1); // return True
 * myCircularQueue.enQueue(2); // return True
 * myCircularQueue.enQueue(3); // return True
 * myCircularQueue.enQueue(4); // return False
 * myCircularQueue.Rear();     // return 3
 * myCircularQueue.isFull();   // return True
 * myCircularQueue.deQueue();  // return True
 * myCircularQueue.enQueue(4); // return True
 * myCircularQueue.Rear();     // return 4
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= k <= 1000
 * 0 <= value <= 1000
 * At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty,
 * and isFull.
 *
 *
*/

// @lc code=start
type MyCircularQueue struct {
	queue []int
	front int
	rear  int
	size  int
}

func Constructor(k int) MyCircularQueue {
	return MyCircularQueue{
		queue: make([]int, k),
		front: -1,
		rear:  -1,
		size:  k,
	}
}

func (this *MyCircularQueue) EnQueue(value int) bool {
	if this.IsFull() {
		return false
	}
	index := (this.rear + 1) % this.size

	this.queue[index] = value
	this.rear = index
	if this.front == -1 {
		this.front = 0
	}
	return true
}

func (this *MyCircularQueue) DeQueue() bool {
	if this.IsEmpty() {
		return false
	}
	if this.front == this.rear {
		this.front = -1
		this.rear = -1
		return true
	}
	index := (this.front + 1) % this.size
	this.front = index
	return true
}

func (this *MyCircularQueue) Front() int {
	if this.IsEmpty() {
		return -1
	}
	return this.queue[this.front]
}

func (this *MyCircularQueue) Rear() int {
	if this.IsEmpty() {
		return -1
	}
	return this.queue[this.rear]

}

func (this *MyCircularQueue) IsEmpty() bool {
	if this.front == -1 || this.rear == -1 {
		return true
	}
	return false
}

func (this *MyCircularQueue) IsFull() bool {
	nextIndex := (this.rear + 1) % this.size
	return nextIndex == this.front
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * obj := Constructor(k);
 * param_1 := obj.EnQueue(value);
 * param_2 := obj.DeQueue();
 * param_3 := obj.Front();
 * param_4 := obj.Rear();
 * param_5 := obj.IsEmpty();
 * param_6 := obj.IsFull();
 */
// @lc code=end

