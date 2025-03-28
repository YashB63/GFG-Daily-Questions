class Solution:  
    def findMaxSum(self,arr):
        a=0
        b=0
        for i in range(len(arr)):
            if i%2==0:
                a=max(a+arr[i],b)
            else:
                b=max(b+arr[i],a)
        return max(a,b)