class Solution:
    def smallestNumber(self, s, d):
        maxsum=d*9
        low=1
        if s>d*9:
            return -1
        ans=0
        for i in range(1,10):
            if s-i<=(d-1)*9:
                ans+=i
                s-=i
                d-=1
                break
        if d:
            ans=ans*(10**(d))
        cur=1
        while d and s and s<=d*9:
            for i in range(9,0,-1):
                if s-i>=0 and s-i<=(d-1)*9:
                    ans+=(i*cur)
                    s-=i
                    d-=1
                    break
            cur*=10
        return ans