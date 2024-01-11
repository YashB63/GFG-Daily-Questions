class Solution:
    
    def celebrity(self, M, n):
         
        i = 0
        for j in range(n):
            if i == j:
                continue
            
            if M[i][j]:
                i = j
        
        for j in range(n):
            
            if i == j:
                continue
                
            if (M[j][i] == 1) and (M[i][j] == 0):
                i = i
            else:
                i = -1
                break
            
        return i