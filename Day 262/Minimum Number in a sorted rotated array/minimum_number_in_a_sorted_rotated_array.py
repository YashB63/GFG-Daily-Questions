class Solution:
    def minNumber(self, arr,low,high):
        n=len(arr)
        low=0
        high=n-1
        mini=999999999999999
        while low<high:
            
            mini=min(mini,min(arr[low],arr[high]))
            low+=1
            high-=1
        return mini