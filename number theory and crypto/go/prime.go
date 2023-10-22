package main
import (
	"fmt"
	"math"
)

func isPrime(n int) bool {
	if n < 2 {
		return false
	}
	if n == 2 {
		return true
	}
	// Loop up to the square root of n
	for i := 3; i <= int(math.Sqrt(float64(n))); i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func sieve(n int) []int {
	// Declare an array of n+1 elements
	var primes = make([]int, n+1)

	// Initialize the array with 1
	for i := 0; i <= n; i++ {
		primes[i] = 1
	}

	primes[0] = 0
	primes[1] = 0

	for i := 2; i <= n; i++ {
		if primes[i] == 1 {
			for j := i * i; j <= n; j += i {
				primes[j] = 0
			}
		}
	}

	return primes
}

func main() {
	fmt.Println(isPrime(5)) // Should print true
	fmt.Println(isPrime(6)) // Should print false
    var primes = sieve(100)
	for i := 0; i < len(primes); i++ {
		if primes[i] == 1 {
			fmt.Printf("%d ", i)
		}
	}
	fmt.Println()
}
