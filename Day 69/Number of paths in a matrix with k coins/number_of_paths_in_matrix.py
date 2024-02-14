class Solution:
    def numberOfPath (self, n, k, arr):
        
        x = {}
        def dfs(r, c, k):
            if max(r, c) >= n or arr[r][c] > k:
                return 0
            if (r, c, k) in x:
                return x[(r, c, k)]
                
            if r == c == n-1:
                return 1 if arr[r][c] == k else 0
            
            right = dfs(r, c+1, k - arr[r][c])
            down = dfs(r+1, c, k - arr[r][c])
            res = x[(r, c, k)] = right + down
            return res
            
        return dfs(0, 0, k)