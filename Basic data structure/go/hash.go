// direct addressing
package main

import "math"

type SimpleHashTable struct {
	data [100]int
}

func (h *SimpleHashTable) Insert(key int) {
	h.data[key] = key
}
func (h SimpleHashTable) Search(key int) int {
	return h.data[key]
}
func (h *SimpleHashTable) Delete(key int) {
	h.data[key] = 0
}
func (h SimpleHashTable) Print() {
	for i := 0; i < len(h.data); i++ {
		if h.data[i] != 0 {
			println(h.data[i])
		}
	}
}

// hashing with chaining
type HashWithChain struct {
	data [100]*LinkedList
}

func (h *HashWithChain) Insert(key int) {
	// mod 100 to avoid index out of range
	index := key % 100
	if h.data[index] == nil {
		h.data[index] = new(LinkedList)
	}
	h.data[index].Insert(key)
}
func (h HashWithChain) Search(key int) int {
	index := key % 100
	if h.data[index] == nil {
		return -1
	}
	node := h.data[index].Search(key)
	if node == nil {
		return -1
	}
	return node.data
}
func (h *HashWithChain) Delete(key int) {
	index := key % 100
	if h.data[index] == nil {
		return
	}
	h.data[index].Delete(key)
}
func (h HashWithChain) Print() {
	for i := 0; i < len(h.data); i++ {
		if h.data[i] != nil {
			h.data[i].Print()
		}
	}
}

// define constant A as the golden ratio
const A = 0.618033

type MultiplicativeHash struct {
	data [100]int
}

// hash function that takes a key and returns an index
func (h *MultiplicativeHash) hash(key int) int {
	// multiply key and A, take the fractional part, multiply by table size, and take the floor
	return int(math.Floor(float64(len(h.data)) * math.Mod(float64(key)*A, 1)))
}

// insert function that takes a key and a value and stores them in the hash table
func (h *MultiplicativeHash) insert(key, value int) {
	// compute the initial index using the hash function
	index := h.hash(key)
	// loop until an empty slot is found
	for h.data[index] != 0 {
		// increment the index using linear probing
		index = (index + 1) % len(h.data)
	}
	// store the value in the slot
	h.data[index] = value
}

// search function that takes a key and returns the value associated with it, or -1 if not found
func (h *MultiplicativeHash) search(key int) int {
	// compute the initial index using the hash function
	index := h.hash(key)
	// loop until the key is found or an empty slot is reached
	for h.data[index] != 0 {
		// check if the slot contains the value for the key
		if h.data[index] == key {
			// return the value
			return h.data[index]
		}
		// increment the index using linear probing
		index = (index + 1) % len(h.data)
	}
	// return -1 to indicate not found
	return -1
}

// delete function that takes a key and removes it from the hash table, if present
func (h *MultiplicativeHash) delete(key int) {
	// compute the initial index using the hash function
	index := h.hash(key)
	// loop until the key is found or an empty slot is reached
	for h.data[index] != 0 {
		// check if the slot contains the value for the key
		if h.data[index] == key {
			// set the slot to zero to indicate empty
			h.data[index] = 0
			return // exit the function
		}
		// increment the index using linear probing
		index = (index + 1) % len(h.data)
	}
}

func main() {
	// MultiplicativeHash
	h := new(MultiplicativeHash)
	h.insert(1, 1)
	h.insert(2, 2)
	h.insert(3, 3)
	h.insert(4, 4)
	h.insert(5, 5)
	h.insert(6, 6)
	println(h.search(1))
	println(h.search(5))
	h.delete(5)
	println(h.search(5))
	println(h.search(8))

}
