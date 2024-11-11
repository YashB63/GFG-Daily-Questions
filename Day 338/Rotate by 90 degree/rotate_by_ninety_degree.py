def rotate(mat): 
    n=len(mat)
    for i in range(n):
        for j in range(i+1,n):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
    for i in range(n):
        mat[i] = mat[i][::-1] 
    return mat