import math
def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True

def digitsAddUpToTen(n):
    n = str(n)
    total = 0
    for i in range(len(n)):
        total += int(n[i])
    return total == 10 and n[-2]=='3'

#pseudoprime
total=0
for n in range(2, 1000):
    if(not isPrime(n)):
        if(((2**n)-2)%n==0):
            total+=1

print("total ",total)
