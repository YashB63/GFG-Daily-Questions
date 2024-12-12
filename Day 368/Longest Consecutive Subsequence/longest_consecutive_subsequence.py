class Solution:
    
    def findLongestConseqSubseq(self,arr):
        s=set()
        for i in arr:
            s.add(i)
        ans=float('-inf')
        for i in s:
            if i-1 not in s:
                c=0
                while i in s:
                    c+=1
                    i+=1
                ans=max(ans,c)
        return ans