class Solution:
    def ValidTrack(self, arr):
        n=len(arr)
        mid=n//2
        if arr[mid]!=1:
            return False
        
        i=0 
        j=n-1
        while i <j:
            if arr[i]!=arr[j]:
                return False
            i=i+1
            j=j-1
        
        diff=abs(arr[1]-arr[0])
        
        for i in range(0,n-1):
            if abs(arr[i+1]-arr[i])!=diff:
                return False
        return True