class Solution:
    def preprocess(self,arr, N, left, right): 
        left[0] = 0
        lastIncr = 0
      
        for i in range(1,N): 
            if (arr[i] > arr[i - 1]): 
                lastIncr = i 
            left[i] = lastIncr 
      
        right[N - 1] = N - 1
        firstDecr = N - 1
      
        i = N - 2
        while(i >= 0): 
            if (arr[i] > arr[i + 1]): 
                firstDecr = i 
            right[i] = firstDecr 
            i -= 1
      
    def isSubarrayMountainForm(self,arr, left, right, L, R): 
        return (right[L] >= left[R]) 
    
    def processqueries(self,arr,n,m,q):
        result=[]
        left = [0 for i in range(n)] 
        right = [0 for i in range(n)] 
        self.preprocess(arr, n, left, right)
        for i in q:
            L,R=i
            if (self.isSubarrayMountainForm(arr, left, right, L, R)): 
                result.append("Yes")
            else:
                result.append("No")
        return result