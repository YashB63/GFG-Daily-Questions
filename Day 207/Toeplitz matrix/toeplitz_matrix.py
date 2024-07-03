def isToeplitz(mat):
    
    def is_diagnal(row, col):
        val = mat[row][col]
        
        while row<len(mat) and col<len(mat[0]):
            if mat[row][col] != val:
                return False
            row +=1
            col +=1
        return True
        
    for i in range(len(mat[0])):
        if not is_diagnal(0, i):
            return False
    for i in range(1, len(mat)):
        if not is_diagnal(i, 0):
            return False
    return True