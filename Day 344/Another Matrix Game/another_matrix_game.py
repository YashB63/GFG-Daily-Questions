class Solution:
    def matrixGame(self, S):
        ln = len(S)
        n = int(ln**0.5)
        mat = [["" for _ in range(n)] for _ in range(n)]
        
        ind = 0
        ans = ""
        

        for y in range(n):
            for x in range(n):
                mat[y][x] = S[ind]
                
                ind+=1
        res = [] 
        
        for x in range(n):
            dc = dict()
            ls = []
            
            
            for y in range(n):
                if mat[y][x] not in dc:
                    dc[mat[y][x]] = 1
                    
                else:
                    dc[mat[y][x]]+=1
            for y in range(n):
                
                if dc[mat[y][x]] == 1:
                    ls.append(mat[y][x])
                    
            row = ""
            ln = len(ls)
            
            for i in range(ln//2):
                row += ls[i]
                row += ls[-1-i]
                
            if ln&1:
                row +=ls[ln//2]
            ans +=row
        return ans if ans else "0"