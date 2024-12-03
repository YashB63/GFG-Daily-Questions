class Solution:
    def missingNumber(self,arr):
        arr.sort()
        res=1
        for i in arr:
            if i==res:
                res+=1
            elif i>res:
                break
        return res