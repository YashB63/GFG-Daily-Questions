class Solution:
    def isSubsetSum (self, arr, sum): 
        n = len(arr)
        d= [[False for _ in range(sum + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            d[i][0] = True
        for i in range(1, n + 1):
            for j in range(1, sum + 1):
                if arr[i - 1] > j:
                    d[i][j] = d[i - 1][j]
                else:
                    d[i][j] = d[i - 1][j] or d[i - 1][j - arr[i - 1]]
        
        return d[n][sum]