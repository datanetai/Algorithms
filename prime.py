#implement sieve of eratosthenes
def sieve(n):
    nums = [True] * n
    nums[0] = False
    nums[1] = False
    for i in range(2, n):
        if nums[i]:
            for j in range(i*i, n, i):
                nums[j] = False
    return [i for i in range(n) if nums[i]]

#test sieve
print(sieve(100))

#algorithm to find prime factors
def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    return factors

#test prime factors
print(prime_factors(55))

#algorithm to check if a number is prime
import math
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    for i in range(3, int(math.sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True

#test is_prime
print(is_prime(11))

#fermat primality test
import random
def is_prime_fermat(n, k=5):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    for i in range(k):
        a = random.randrange(2, n-1)
        if pow(a, n-1, n) != 1:
            return False
    return True
#remove comma from string
def remove_comma(s):
    return s.replace(',', '')
#time is_prime_fermat
import time
start = time.time()
print(is_prime_fermat(int(remove_comma(input('Enter a number: ')))))
end = time.time()
print(end - start)
