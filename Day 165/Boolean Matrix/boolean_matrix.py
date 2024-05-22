def booleanMatrix(matrix):
    
    R = len(matrix)
    C = len(matrix[0])
    
    row = [False]*R
    col = [False]*C
    
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 1:
                row[i] = True
                col[j] = True
                
    for i in range(R):
        for j in range(C):
            if row[i] or col[j]:
                matrix[i][j] = 1