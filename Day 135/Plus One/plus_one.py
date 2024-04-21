class Solution:
    def increment(self, arr, N):
        
        ans=''
        for i in arr:
            ans=ans+str(i)
        res=int(ans)+1
        result =list(map(int, str(res)))
        return result