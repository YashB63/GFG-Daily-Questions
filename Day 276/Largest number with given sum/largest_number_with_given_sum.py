class Solution:
    
    def largestNum(self,n,s):
        if n*9>=s:
            ans=''
            while(s>=9):
                s=s-9
                ans+='9'
            if s>0:
                ans+=str(s)
            x=len(ans)
            for i in range(n-x):
                ans+='0'
            return ans
        else:
            return -1