class Solution:
    def longestUniqueSubstr(self, s):
        n=len(s)
        l=0
        r=0
        ans=0
        arr=[0]*128
        
        while(r<n):
            
            if arr[ord(s[r])]!=0:
                arr[ord(s[l])]-=1
                l+=1
            else :
                arr[ord(s[r])]+=1
                ans=max(ans,r-l+1)
                r+=1
                
        return ans