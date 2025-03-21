class Solution:
    def countPairs (self, n, arr, k):
        d={}
        ans=0
        for i in arr:
            if i%k in d:
                d[i%k]+=1
            else:
                d[i%k]=1
        for i in d:
            if(d[i]>1):
                ans=ans+(d[i]*(d[i]-1)//2)
        return ans