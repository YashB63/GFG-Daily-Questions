class Solution:
    
    def mergeKArrays(self, arr, K):
        
        res=[]
        for i in arr:
            res=res+i
        res.sort()
        return res