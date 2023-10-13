// is prime
function isPrime(n) {
    if (n < 2) return false;
    else if (n == 2) return true;
    else if (n % 2 == 0) return false;
    for (let i = 3; i <= Math.sqrt(n); i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}
function sieve(n) {
    // declare array upto n 
    let arr = new Array(n + 1).fill(true);
    // 0 and 1 are not prime
    arr[0] = arr[1] = false;
    // iterate upto sqrt(n)
    for (let i = 2; i <= Math.sqrt(n); i++) {
        // if i is prime
        if (arr[i]) {
            // mark all multiples of i as false
            for (let j = i * i; j <= n; j += i) {
                arr[j] = false;
            }
        }
    }
    // return array of prime numbers
    return arr;
}
// test
console.log(isPrime(49));

let n = 100;
let primes = sieve(n);
for (let i = 0; i <= n; i++) {
    if (primes[i]) console.log(i);
}

function test() {
    // we will use sieve to generate prime numbers upto 100 and then check it against isPrime function
    let n = 100;
    let primes = sieve(n);
    for (let i = 0; i <= n; i++) {
        if (primes[i] != isPrime(i)) {
            // raise exception
            throw new Error("Test failed");
        }
    }
}