class Solution:
    def countSpecials(self, k, arr):
        a=len(arr)//k
        fre=Counter(arr)
        ans=0
        for i in fre.values():
            if i==a:
                ans+=1
        return ans