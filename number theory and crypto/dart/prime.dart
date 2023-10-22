  import 'dart:math';
  void main () {
    print(isPrime(2));
    print(isPrime(3));
    print(isPrime(9));
    List<int> primes = sieve(100);
    for (int i=0; i<primes.length; i++) {
      if (primes[i] == 1) print(i);
    }
  }

  bool isPrime(int n) {
    if (n<2) return false;
    else if (n == 2) return true;
    else if (n%2 == 0) return false;
    for (int i=3; i<=sqrt(n); i+=2) {
      if (n%i == 0) return false;
    }
    return true;
  }

  // sieve of eratosthenes
  List<int> sieve(int n) {
    // Declare a list of n+1 elements
    List<int> primes = List<int>.filled(n + 1, 1);

    // Initialize elements at index 0 and 1 to 0
    primes[0] = 0;
    primes[1] = 0;

    // Start from 2 and go up to n to find prime numbers
    for (int i = 2; i <= n; i++) {
      if (primes[i] == 1) {
        // Mark multiples of i as not prime
        for (int j = i * i; j <= n; j += i) {
          primes[j] = 0;
        }
      }
    }

    return primes;
  }


