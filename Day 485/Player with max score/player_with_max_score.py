class Solution:
    def is1winner (self, n, arr):
        dp = [[-1]*n for _ in range(n)]
        player1 = self.func(arr,0,n-1,dp)
        player2 = sum(arr) - player1
        if player1>=player2:
            return 1
        return 0
        
    def func(self,arr,start,end,dp):
        if start>end:
            return 0
        if start==end:
            return arr[start]
        if end-start==1:
            return max(arr[start],arr[end])
        if dp[start][end]!=-1:
            return dp[start][end]
        left = arr[start]+min(self.func(arr,start+2,end,dp),self.func(arr,start+1,end-1,dp))
        right = arr[end]+min(self.func(arr,start,end-2,dp),self.func(arr,start+1,end-1,dp))
        dp[start][end] = max(left,right)
        return dp[start][end]