import math

class Solution:
    def subsetXOR(self, arr, N, K): 
        max_ele = arr[0] 
        for i in range(1, N): 
            if arr[i] > max_ele : 
                max_ele = arr[i] 
                  
        m = (1 << (int)(math.log2(max_ele) + 1)) - 1
        if( K > m  ): 
           return 0
      
        dp = [[0 for i in range(m + 1)] 
                 for i in range(N + 1)] 
          
        dp[0][0] = 1
      
        for i in range(1, N + 1): 
            for j in range(m + 1): 
                dp[i][j] = (dp[i - 1][j] + 
                            dp[i - 1][j ^ arr[i - 1]]) 
      
        return dp[N][K] 