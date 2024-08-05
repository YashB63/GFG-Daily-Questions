from typing import List

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        all_paths = []
        
        def helper(mat, i, j, n, path):
            if i == n-1 and j == n-1:
                all_paths.append(path)
                return
            
            mat[i][j] = 2
        
            if i+1 < n and mat[i+1][j] == 1:
                helper(mat, i+1, j, n, path+'D')
                
            
            if j+1 < n and mat[i][j+1] == 1:
                helper(mat, i, j+1, n, path+'R')
            
            
            if i-1 >= 0 and mat[i-1][j] == 1:
                helper(mat, i-1, j, n, path+'U')
                
            
            if j-1 >= 0 and mat[i][j-1] == 1:
                helper(mat, i, j-1, n, path+'L')
            
            mat[i][j] = 1
        
        
        if m[0][0] != 1:
            return []
            
        helper(m,0,0,len(m),'')
        
        return all_paths