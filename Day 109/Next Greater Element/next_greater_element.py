from collections import deque

class Solution:
    def nextLargerElement(self,arr,n):
        
        s = deque()
        res =[0]*n
        for i in range(n-1,-1,-1):
            while (len(s) and s[-1] <= arr[i]):
                s.pop()
            
            if (not len(s)):
                res[i] = -1
            else:
                res[i] = s[-1]
            
            s.append(arr[i])
            
        return res