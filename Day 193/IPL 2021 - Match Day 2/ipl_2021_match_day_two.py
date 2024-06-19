from collections import deque

class Solution:
    def max_of_subarrays(self,arr,n,k):
        
        result=[]
        q=deque()
        l,r=0,0
        for i in range(n):
            while q and arr[q[-1]]<arr[i]:
                q.pop()
            q.append(i)
            if l>q[0]:
                q.popleft()
            if r+1>=k:
                result.append(arr[q[0]])
                l+=1
            r+=1
        return result