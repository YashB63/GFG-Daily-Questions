class Solution:
    def smallestSubWithSum(self, x, arr):
        n=len(arr)
        ml=float('inf')
        start,cs=0,0
        for end in range(n):
            cs+=arr[end]
            while cs>x:
                ml=min(ml,end-start+1)
                cs-=arr[start]
                start+=1
        return ml if ml!=float('inf') else 0