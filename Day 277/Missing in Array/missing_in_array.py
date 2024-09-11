class Solution:
    def missingNumber(self, n, arr):
        s=(n*(n+1))//2
        i=0
        while(i<n-1):
            s-=arr[i]
            i+=1
        return s