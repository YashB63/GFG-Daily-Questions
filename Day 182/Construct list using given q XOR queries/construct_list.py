from typing import List

class Solution:
    def constructList(self, q : int, queries : List[List[int]]) -> List[int]:
        
        val=0
        ans=[]
        for i in range(q-1,-1,-1):
            if queries[i][0]:
                val^=queries[i][1]
            else:
                queries[i][1]^=val
                ans.append(queries[i][1])
        ans.append(val)
        ans.sort()
        return ans