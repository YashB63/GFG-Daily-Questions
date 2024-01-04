from typing import List


class Solution:
    def isPossible(self, N : int, coins : List[int]) -> bool:
     
        x = [[0]*(N + 1) for _ in range(2025)]
        
        for i in range(N + 1):
            x[0][i] = True
        
        for y in range(1, 2025):
            for i in range(N):
                x[y][i + 1] = x[y][i]
                
                if y >= coins[i]:
                    x[y][i + 1] = x[y][i + 1] or x[y - coins[i]][i]
                
                if x[y][i + 1] and (y%20 == 0 or y%24 == 0 or y == 2024):
                    return True
                    
        return False
