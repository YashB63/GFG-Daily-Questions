import math

class Solution:
    def matrixChainOrder(self, p, n):
        
        inf = math.inf
        cost = [[inf for _ in range(n)] for _ in range(n)]
        brac = [['' for _ in range(n)] for _ in range(n)]
        
        for i in range(n-1):
            cost[i][i + 1] = 0
            brac[i][i + 1] = chr(ord('A') + i)
            
        for i in range(2, n):
            for j in range(n - i):
                x = i + j
                for k in range(j + 1, n):
                    if cost[j][x] > cost[j][k] + cost[k][x] + p[j] * p[x] * p[k]:
                        cost[j][x] = cost[j][k] + cost[k][x] + p[j] * p[x] * p[k]
                        brac[j][x] = '(' + brac[j][k] + brac[k][x] + ')'
                        
        return brac[0][n - 1]