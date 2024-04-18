class Solution:
    
    def BoundaryTraversal(self,matrix, n, m):
         
        lis = []
        
        lis = lis + matrix[0]
        
        for i in matrix[1:-1]:
            lis.append(i[-1])
            
        if n > 1:
            lis += matrix[-1][::-1]
        if m > 1:
            for i in matrix[1:-1][::-1]:
                lis.append(i[0])
        
        return lis