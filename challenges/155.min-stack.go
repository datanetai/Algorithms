/*
 * @lc app=leetcode id=155 lang=golang
 *
 * [155] Min Stack
 *
 * https://leetcode.com/problems/min-stack/description/
 *
 * algorithms
 * Medium (53.27%)
 * Likes:    13312
 * Dislikes: 805
 * Total Accepted:    1.5M
 * Total Submissions: 2.8M
 * Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n' +
  '[[],[-2],[0],[-3],[],[],[],[]]'
 *
 * Design a stack that supports push, pop, top, and retrieving the minimum
 * element in constant time.
 *
 * Implement the MinStack class:
 *
 *
 * MinStack() initializes the stack object.
 * void push(int val) pushes the element val onto the stack.
 * void pop() removes the element on the top of the stack.
 * int top() gets the top element of the stack.
 * int getMin() retrieves the minimum element in the stack.
 *
 *
 * You must implement a solution with O(1) time complexity for each
 * function.
 *
 *
 * Example 1:
 *
 *
 * Input
 * ["MinStack","push","push","push","getMin","pop","top","getMin"]
 * [[],[-2],[0],[-3],[],[],[],[]]
 *
 * Output
 * [null,null,null,null,-3,null,0,-2]
 *
 * Explanation
 * MinStack minStack = new MinStack();
 * minStack.push(-2);
 * minStack.push(0);
 * minStack.push(-3);
 * minStack.getMin(); // return -3
 * minStack.pop();
 * minStack.top();    // return 0
 * minStack.getMin(); // return -2
 *
 *
 *
 * Constraints:
 *
 *
 * -2^31 <= val <= 2^31 - 1
 * Methods pop, top and getMin operations will always be called on non-empty
 * stacks.
 * At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
 *
 *
*/
// for second way check out your submissions
// @lc code=start
type Node struct {
	Val  int
	Next *Node
	Min  int
}
type MinStack struct {
	stack  *Node
	length int
}

func Constructor() MinStack {
	return MinStack{}
}

func (this *MinStack) Push(val int) {
	if this.stack == nil {
		this.stack = &Node{Val: val, Min: val}
	} else {
		newNode := &Node{Val: val, Min: min(val, this.stack.Min)}
		newNode.Next = this.stack
		this.stack = newNode
	}
	this.length++
}

func (this *MinStack) Pop() {

	this.stack = this.stack.Next
	this.length--
}

func (this *MinStack) Top() int {
	return this.stack.Val
}

func (this *MinStack) GetMin() int {
	return this.stack.Min
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
// @lc code=end

