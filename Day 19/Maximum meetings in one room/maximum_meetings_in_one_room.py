from typing import List


class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        
        x = []
        for i in range(N):
            x.append([S[i], F[i], i+1])
            
        x.sort(key = lambda x: x[1])
        
        res = [x[0][2]]
        end = x[0][1]
        
        for i  in range(1, len(x)):
            if x[i][0] > end:
                res.append(x[i][2])
                end = x[i][1]
                
        res.sort()
        return res