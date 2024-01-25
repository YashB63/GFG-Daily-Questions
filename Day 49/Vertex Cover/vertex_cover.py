from typing import List

class Solution:
    def vertexCover(self, n : int, edges : List[List[int]]) -> int:
        
        def util(edges):
            if not edges:
                return 0
                
            x, y = [], []
            
            for i in edges:
                if not(i[0] == edges[0][0] or i[1] == edges[0][0]):
                    x.append(i)
                
                if not(i[0] == edges[0][1] or i[1] == edges[0][1]):
                    y.append(i)
                    
            return min(util(x) + 1, util(y) + 1)
            
        return util(edges)