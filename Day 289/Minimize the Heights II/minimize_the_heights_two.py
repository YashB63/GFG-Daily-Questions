class Solution:
    def getMinDiff(self, arr,k):
        n=len(arr)
        arr.sort()
        result=arr[-1]-arr[0]
        small=arr[0]+k
        large=arr[-1]-k
        if small>large:
            small, large=large, small
        for i in range(n):
            min_height=min(small, arr[i]-k)
            max_height=max(large, arr[i-1]+k)
            if min_height < 0:
                continue
            result=min(result, max_height-min_height)
        return result