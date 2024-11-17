class Solution:
    def minIncrements(self, arr): 
        arr.sort()
        s=sum(arr)
        for i in range(1,len(arr)):
            if arr[i]<=arr[i-1]:
                arr[i]=arr[i-1]+1
        return sum(arr)-s