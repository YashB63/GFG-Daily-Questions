class Solution:
    
    def CombinationSum2(self, arr, n, k):
        
        ress=set()
        def utility(i,k,cur):
            if k==0:
                ress.add(tuple(sorted(cur)))
            if k<0 or i>=n:
                return
            for j in range(i,n):
                utility(j+1,k-arr[j],cur+(arr[j],))
                
        utility(0,k,())
        
        return sorted(ress)