class Solution:
    def findNumberOfTriangles(self, arr, n):
        arr=sorted(arr)
        count=0
        for k in range(n-1,1,-1):
            i=0
            j=k-1
            while i<j:
                if arr[i]+arr[j]>arr[k]:
                    count+=j-i
                    j-=1
                else:
                    i+=1
        return count