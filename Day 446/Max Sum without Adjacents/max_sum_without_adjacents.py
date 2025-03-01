class Solution:
	def solve(self,arr,n,dp):
        if n==0:
            return arr[0]
        if n<0:
            return 0
        if dp[n]!=-1:
            return dp[n]
        inc=self.solve(arr,n-2,dp)+arr[n]
        exc=self.solve(arr,n-1,dp)+0
        dp[n]=max(inc,exc)
        return dp[n]
        
	def findMaxSum(self,arr, n):
        dp=[-1]*n
        return self.solve(arr,n-1,dp)