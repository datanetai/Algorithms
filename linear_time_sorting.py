#counting sort
def counting_sort(A):
    B = [0] * len(A)
    C = [0] * (max(A) + 1)
    for i in range(len(A)):
        C[A[i]] += 1
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    for i in range(len(A) - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    return B
#there are other linear time sorting algorithms
#like radix sort and bucket sort
#test
assert counting_sort([4,3,2,6,4,2])==[2,2,3,4,4,6]

