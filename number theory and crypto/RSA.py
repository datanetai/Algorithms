#RSA


P=1223
Q=1987
E=948047 #gcd(e, (p − 1)(q − 1)) = gcd(948047, 2426892) = 1.
N=P*Q

def encrypt(m,E,N):
    return m**E % N
def decrypt(c,D,N):
    return c**D % N
def linear_congruence(a, b, m):
    if b == 0:
        return 0

    if a < 0:
        a = -a
        b = -b

    b %= m
    while a > m:
        a -= m

    return (m * linear_congruence(m, -b, a) + b) // a

m=1070777
c=encrypt(m,E,N)
print("ciphertext:",c)
#now solve E*D=1 mod(N-1)
D=linear_congruence(E,1,(P-1)*(Q-1))
m2=decrypt(c,D,N)
print("plaintext:",m2)