from typing import List

class Solution:
    def kthSmallestNum(self, n : int, ranges : List[List[int]], q : int, queries : List[int]) -> List[int]:
        prev_start = 0
        prev_end = 0
        ranges = sorted(ranges,key = lambda x:x[0])
        merged = [ranges[0]]
        for i in range(1,n):
            prev = merged[-1]
            curr = ranges[i]
            if curr[0]>=prev[0] and curr[0]<=prev[1] and curr[1]>prev[1]:
                merged[-1][1] = curr[-1]
            elif curr[0]>prev[1]:
                merged.append(curr)
        
        ans = []
        for query in queries:
            for r in merged:
                start = r[0]
                end = r[1]
                if query<=(end-start+1):
                    ans.append(start+query-1)
                    query = 0
                    break
                else:
                    query -= end-start+1
            if query>0:
                ans.append(-1)
        return ans