class Solution:
    def optimalStrategyOfGame(self,n, arr):
        
        hash_map={}
        def solve(i,j):
            if i>j or i>=n or j<0:
                return 0
            k=(i,j)
            if k in hash_map:
                return hash_map[k]
            opt1=arr[i]+min(solve(i+2,j),solve(i+1,j-1))
            opt2=arr[j]+min(solve(i,j-2),solve(i+1,j-1))
            
            hash_map[k]=max(opt1,opt2)
            return hash_map[k]
        return solve(0,n-1)