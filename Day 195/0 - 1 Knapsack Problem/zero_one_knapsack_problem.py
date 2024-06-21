class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        dp = [0 for i in range(W+1)] 
    
        for i in range(1, n+1): 
            for w in range(W, 0, -1): 
                                    
                if wt[i-1] <= w:
                   
                    dp[w] = max(dp[w], dp[w-wt[i-1]]+val[i-1])
    
        return dp[W]