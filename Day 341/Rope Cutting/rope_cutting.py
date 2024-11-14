class Solution:
    def RopeCutting(self, arr):
        n=len(arr)
        i=0
        result=[]
        arr.sort()
        while i<n:
            if i>0:
                result.append(n-i)
            current_length=arr[i]
            while i<n and arr[i]==current_length:
                i+=1
        return result