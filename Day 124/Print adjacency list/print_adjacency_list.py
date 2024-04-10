from typing import List

class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        
        counter={i:[] for i in range(V)}
        
        N=len(edges)
        
        for i in range(N):
            node=edges[i]
            
            counter[node[0]].append(node[1])
            counter[node[1]].append(node[0])
        
        values=counter.values()
        
        return values