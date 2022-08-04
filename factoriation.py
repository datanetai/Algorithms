#fermat factorization
import math
def fermat(n):
    a=math.ceil(math.sqrt(n))
    b=math.ceil(math.sqrt(n))
    b2=a*a-n
    count=0
    while not b*b!=b2:
        a+=1
        b2=a*a-n
        count+=1
    return a+math.sqrt(b2),a-math.sqrt(b2)

def is_square(n):
    return math.sqrt(n)%1==0

#naive factorization
def naive_factorization(n):
    factors=[]
    for i in range(2,n):
        if n%i==0:
            factors.append(i)
    return factors
#test fermat
def test_naive():
    print("Testing fermat...")
    print("100032 =", naive_factorization(100032))
    print("3232 =", naive_factorization(3232))
    print("323 =", naive_factorization(323))
    print("3231 =", naive_factorization(3231))
    print("431434=", naive_factorization(431434))
    print("983744 =", naive_factorization(983744))
    print("434343 =", naive_factorization(434343))
    print("434343 =", naive_factorization(434343))
    print("100000000 =", naive_factorization(100000000))
    print("34 =", naive_factorization(34))
    print("43434 =", naive_factorization(43434))
    print("43443 =", naive_factorization(43443))
    print("2212 =", naive_factorization(2212))
    print("97 =", naive_factorization(97))
    print("6565 =", naive_factorization(6565))
    print("9999 =", naive_factorization(9999))
    print("18 =", naive_factorization(18))
    print("76767 =", naive_factorization(76767))
    print("1001 =", naive_factorization(1001))
    print("333333333 =", naive_factorization(333333333))
    print("44552211 =", naive_factorization(44552211))
    
def test_fermat():
    print("Testing naive...")
    print("100032 =", fermat(100032))
    print("3232 =", fermat(3232))
    print("323 =", fermat(323))
    print("3231 =", fermat(3231))
    print("431434=", fermat(431434))
    print("983744 =", fermat(983744))
    print("434343 =", fermat(434343))
    print("434343 =", fermat(434343))
    print("100000000 =", fermat(100000000))
    print("34 =", fermat(34))
    print("43434 =", fermat(43434))
    print("43443 =", fermat(43443))
    print("2212 =", fermat(2212))
    print("97 =", fermat(97))
    print("6565 =", fermat(6565))
    print("9999 =", fermat(9999))
    print("18 =", fermat(18))
    print("76767 =", fermat(76767))
    print("1001 =", fermat(1001))
    print("333333333 =", fermat(333333333))
    print("44552211 =", fermat(44552211))
    
#time test_fermat()
import time
start=time.time()
test_fermat()
end=time.time()
print("Time:",end-start)

start=time.time()
test_naive()
end=time.time()
print("Time:",end-start)