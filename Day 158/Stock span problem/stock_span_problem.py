class Solution:
    
    def calculateSpan(self,a,n):
        
        def ngeLeft(arr,n):
            nge = []
            ans = []
            for i in range(n):
                while len(nge) > 0 and arr[i] >= arr[nge[-1]]:
                    nge.pop()
                
                if len(nge) == 0:
                    ans.append(-1)
                else:
                    ans.append(nge[-1])
                
                nge.append(i)
            
            return ans
        
        nge = ngeLeft(a,n)
        span = [0]*n
        for i in range(n):
            span[i] = i - nge[i]
        
        return span