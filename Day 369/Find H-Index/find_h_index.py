class Solution:
    def hIndex(self, citations):
        n=len(arr)
        index=0
        arr.sort(reverse=True)
        for i,val in enumerate(arr):
            if(val>=i+1):
                index=i+1
            else:
                break
        return index