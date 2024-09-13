class Solution:
    def getSingle(self,arr):
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for key,value in d.items():
            if value%2!=0:
                return key