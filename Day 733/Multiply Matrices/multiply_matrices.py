def multiply(A, B, C, n):
    for i in range(n):
        for j in range(n):
            total=0
            for k in range(n):
                total+=A[i][k]*B[k][j]
            C[i][j]=total