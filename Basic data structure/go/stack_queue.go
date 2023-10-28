// stack implementation
package main

import (
	"errors"
	"fmt"
)

type Stack struct {
	elements []interface{}
}

func (s *Stack) Push(e interface{}) {
	s.elements = append(s.elements, e)
}

func (s *Stack) Pop() (interface{}, error) {
	if len(s.elements) == 0 {
		return nil, errors.New("Empty stack!")
	}
	e := s.elements[len(s.elements)-1]
	s.elements = s.elements[:len(s.elements)-1]
	return e, nil
}

// check if Empty
func (s *Stack) isEmpty() bool {
	return len(s.elements) == 0
}

// queue
type Queue struct {
	elements []interface{}
}

func (q *Queue) enequeue(e interface{}) {
	q.elements = append(q.elements, e)
}

func (q *Queue) dequeue() (interface{}, error) {
	if len(q.elements) == 0 {
		return nil, errors.New("Empty queue!")
	}
	e := q.elements[0]
	q.elements = q.elements[1:]
	return e, nil
}

// check if Empty
func (q *Queue) isEmpty() bool {
	return len(q.elements) == 0
}

func main() {
	// For stack
	s := new(Stack)
	var stackElements []interface{}
	s.Push(1)
	s.Push(2)
	s.Push(3)
	s.Push(4)
	s.Push(5)
	for !s.isEmpty() {
		e, _ := s.Pop()
		stackElements = append(stackElements, e)
	}
	fmt.Println("Stack elements:", stackElements)

	// For queue
	q := new(Queue)
	var queueElements []interface{}
	q.enequeue(1)
	q.enequeue(2)
	q.enequeue(3)
	q.enequeue(4)
	q.enequeue(5)
	for !q.isEmpty() {
		e, _ := q.dequeue()
		queueElements = append(queueElements, e)
	}
	fmt.Println("Queue elements:", queueElements)

}
