class Solution:
    def maxCoins(self,arr, n):
        memo = [[-1]*(n) for _ in range(n)]
        
        def get_max_coins(i, j):
            if i > j:
                return 0
                
            if memo[i][j] != -1:
                return memo[i][j]
                
            left = arr[i] + min(get_max_coins(i+1, j-1), get_max_coins(i+2, j))
            right = arr[j] + min(get_max_coins(i, j-2), get_max_coins(i+1, j-1))
        
            memo[i][j] = max(left, right)
            return memo[i][j]
        
        return get_max_coins(0, n-1)