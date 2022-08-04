#order of integer mod m

from contextlib import nullcontext


def order(m,a=2):
    b=1
    while (True):
        if (a**b)%m==1:
            return b
        b+=1

print("order of integer mod m {}".format(order(35)))
def relatively_prime(n):
    l=[]
    for i in range(2,n):
        if gcd(n,i)==1:
            l.append(i)
    return l
    
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

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

def phi_n(n):
    if isPrime(n):
        return n-1
    
    count = 0
    for i in range(1, n):
        if(gcd(i, n) == 1):
            count += 1
    return count

def primitive_root(m):
    l=relatively_prime(m)
    roots=[]
    phi=phi_n(m)
    for g in l:
        if order(m,g)==phi:
            print("found one")
            roots.append(g)
    return roots if len(roots)>0 else "{0} does not have primitive root".format(m)

def num_of_roots(m):
    #theorem 8.4 collary
    #every prime have primitive root
    if isPrime(m):
        #theorem 8.6 collary
        return phi_n(m-1)
    roots=primitive_root(m)
    if type(roots)==list:
        return phi_n(phi_n(m))




def index(n):
    r=primitive_root(n)[0]
    for i in range(1,n):
        for j in range(1,n):
            if (r**j)%n==i:
                print("ind {0}={1}".format(i,j))

def discrete_log(p,h):
    p=2
    for i in range(1,p):
        if (h**i)%p==1:
            return i

print(discrete_log(56509,38679))