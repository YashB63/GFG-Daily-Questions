def downwardDiagonal(N, A): 
    
    li=[]
    r=len(A)
    c=len(A[0])
    temp=[[] for _ in range(r+c-1)]
    for i in range(r):
        for j in range(c):
            temp[i+j].append(A[i][j])
    
    for i in range(len(temp)):
        li.extend(temp[i])
    
            
    return li