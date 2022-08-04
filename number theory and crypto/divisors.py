#number theoritic function
#number of divisor of n
import math
def divisors(n):
    if isPrime(n):
        return 2
    divisors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisors += 1
    return divisors

def sum_of_divisor(n):
    if isPrime(n):
        return n+1
    sum = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            sum += i
    return sum

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2==0:
        return False
    for i in range(2, math.sqrt(n)+1):
        if n % i == 0:
            return False
    return True
    
def prime_factor(n):
    if isPrime(n):
        return [n]
    prime_factor = []
    i=2
    while i<=n:
        if n%i==0:
            prime_factor.append(i)
            n=n/i
        else:
            i+=1
    #group the same number with power
    prime_factor_group = []
    j=-1
    for i in prime_factor:
        if j!=-1 and i in prime_factor_group[j]:
            continue
        j+=1
        if prime_factor.count(i)>1:
            prime_factor_group.append((i,prime_factor.count(i)))
        else:
            prime_factor_group.append(i)

    return prime_factor_group



def divisor_from_prime_factor(n):
    #theorem 6.2
    prime_factor_group = prime_factor(n)
    divisor = 1
    for i in prime_factor_group:
        if type(i)==tuple:
            divisor *= i[1]+1
        else:
            divisor *= 2
    return divisor

print(divisor_from_prime_factor(180))
print(divisors(180))