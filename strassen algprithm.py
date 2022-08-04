def matrix_multiply(A,B):
    n=len(A)
    c=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j]+=A[i][k]*B[k][j]
    
    return c

def matrix_multiply_recursive(A,B):
    #recursive messy code
    if type(A) is int:
        return A*B
    else:
        c11=matrix_multiply_recursive(A[0][0],B[0][0])+matrix_multiply_recursive(A[0][1],B[1][0])
        c12=matrix_multiply_recursive(A[0][0],B[0][1])+matrix_multiply_recursive(A[0][1],B[1][1])
        c21=matrix_multiply_recursive(A[1][0],B[0][0])+matrix_multiply_recursive(A[1][1],B[1][0])
        c22=matrix_multiply_recursive(A[1][0],B[0][1])+matrix_multiply_recursive(A[1][1],B[1][1])
        c=[[c11,c12],[c21,c22]]
    return c

#strassen algorithm is so messy so skipped

A=[[1,2],[3,4]]
B=[[5,6],[7,8]]
print(matrix_multiply_recursive(A,B))