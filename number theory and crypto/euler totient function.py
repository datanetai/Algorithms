#check if number is prime
def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

#implement gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#euler totient function
def eulerTotient(n):
    if isPrime(n):
        return n-1
    
    count = 0
    for i in range(1, n):
        if(gcd(i, n) == 1):
            count += 1
    return count

def prime_factor(n):
    #return prime factors without it's power
    if isPrime(n):
        return set([n])
    prime_factor = set()
    i=2
    while i<=n:
        if n%i==0:
            prime_factor.add(i)
            n=n/i
        else:
            i+=1
    return prime_factor

def euler_totient_using_primes(n):
    #theorem 7.3
    prime_factors=prime_factor(n)
    val=n
    for i in prime_factors:
        val*=(1-1/i)
    return int(val)
print(euler_totient_using_primes(35))

#order of integer using euler totient function
def order_of_integer(a,n):
    phi=euler_totient_using_primes(n)
    for i in range(1,phi+1):
        if i % phi == 0:
            if a**i % n == 1:
                return i
    return None

print(order_of_integer(2,17))