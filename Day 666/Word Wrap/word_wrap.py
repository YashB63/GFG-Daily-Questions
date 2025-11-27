class Solution:
    def solveWordWrap(self, arr, k):
        n = len(arr)
        dp = [0] * (n + 1)   

        for i in range(n - 1, -1, -1):
            best = float('inf')
            rem = k - arr[i]          
            j = i
            
            while j < n and rem >= 0:
                cost = 0 if j == n - 1 else rem * rem
                cand = cost + dp[j + 1]
                if cand < best:
                    best = cand

                j += 1
                if j < n:
                    rem -= (arr[j] + 1)

            dp[i] = best

        return dp[0]