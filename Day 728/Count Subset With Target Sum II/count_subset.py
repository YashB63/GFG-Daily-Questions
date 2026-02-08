class Solution:
    def solve(self,arr,n,sums,curr):
        if n==0:
            sums[curr]=sums.get(curr,0)+1
            return
        self.solve(arr,n-1,sums,curr)
        self.solve(arr,n-1,sums,curr+arr[n-1])
        
    def sums(self, arr):
        n=len(arr)
        sums={}
        self.solve(arr,n,sums,0)
        return sums
        
    def countSubset(self, arr, k):
        n=len(arr)
        mid=n//2
        left=arr[:mid]
        right=arr[mid:]
        left_sums=self.sums(left)
        right_sums=self.sums(right)
        ans=0
        for s in left_sums:
            ans+=left_sums[s]*right_sums.get(k-s,0)
        return ans