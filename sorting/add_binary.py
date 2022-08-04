import re


def add_two_binary(A,B):
    # assume both A and B have same length
    #if not we can concatenate 0 to the shorter one
    carry=0
    C=[]
    i=0
    for i in range(len(A)-1,-1,-1):
        C.append((A[i]+B[i]+carry) % 2)
        carry=(A[i]+B[i]+carry) // 2
    C.append(carry)
    C.reverse()

    return C
A=[1,0,1]
B=[1,1,1]
print(add_two_binary(A,B))