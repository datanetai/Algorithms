#check if the number is square free
import math
def isSquareFree(n):
    for i in range(2,round(n**0.5)+1):
        if n%(i**2)==0:
            return False
    return True

#prime factorization 
def factors(n):
    factors=[]
    i=2
    while i<=n:
        if n%i==0:
            factors.append(i)
            n=n//i
        else:
            i+=1
    return factors
#mobius inversion formula
def mobius(n):
    if n==1:
        return 1
    if not isSquareFree(n):
        return 0
    else:
        f=factors(n)
        r=len(f)
        return (-1)**r

def divisors(n):
    divisors=[]
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
#check mobius 
# print(mobius(1))
# print(mobius(2))
# print(mobius(3))
# print(mobius(4))
# print(mobius(5))
# print(mobius(6))
l=divisors(100)
sum_=0
for i in l:
    sum_+=mobius(i)
# note that the sum of mobius is always 0
#by theorem 6.6
print(sum_)