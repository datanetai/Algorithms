# message to integer upto p
import math


def string_to_int(s):
    n=0
    for i in range(len(s)):
        n=n*256+ord(s[i])
    return n %p

def int_to_string(n):
    s=''
    while n>0:
        s=chr(n%256)+s
        n=n//256
    return s





p=467 #must be very large prime
g=2 #maybe primitive root
a,b=0,0
a = 153

def A(p, g):
    A = pow(g, a, p)
    return A
def B(p, g):
    b = 781
    B = pow(g, b, p)
    return B

def shared_key(B,a, p):
    s = pow(B, a, p)
    #or s = pow(A,b,p)
    #both number are same
    return s

#alice calculate A
A=A(p, g)
#random number
import random

m="L"
mi=string_to_int(m)
k=random.randint(0,p)
k=197
c1=pow(g,k,p)
print(c1)
A_k=pow(A,k)
c2=A_k*mi%p
print("c2 {0}".format(c2))
#(c1,c2) is ciphertext
x=pow(c1,p-1-a,p)
m_r=c2*x %p
print(mi,m_r)
m_r=int_to_string(m_r)

print(m_r)