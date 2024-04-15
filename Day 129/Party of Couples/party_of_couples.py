class Solution:
    def findSingle(self, n, arr):
        
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in arr:
            if d[i]%2==1:
                return i
        return -1