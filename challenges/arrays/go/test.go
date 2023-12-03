package main

import "fmt"

// Shape is an interface with two methods: area() and perimeter()
type Shape interface {
	area() float32
	perimeter() float32
}

// Rectangle is a struct that will implement the Shape interface
type Rectangle struct {
	length, breadth float32
}

// Implementing the area() method of the Shape interface for Rectangle
func (r Rectangle) area() float32 {
	return r.length * r.breadth
}

// Implementing the perimeter() method of the Shape interface for Rectangle
func (r Rectangle) perimeter() float32 {
	return 2 * (r.length + r.breadth)
}

// Function that takes a Shape interface as an argument
func calculate(s Shape) {
	fmt.Println("Area:", s.area())
	fmt.Println("Perimeter:", s.perimeter())
}

func main() {
	// Creating a Rectangle instance
	rect := Rectangle{10, 5}

	// Calling the calculate function with a Rectangle, which implements the Shape interface
	calculate(rect)
}
