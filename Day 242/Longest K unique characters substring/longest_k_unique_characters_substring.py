class Solution:

    def longestKSubstr(self, s, k):
        d={}
        length=-1
        left,right=0,0
        while right<len(s):
            if s[right] in d:
                d[s[right]]+=1
            else:
                d[s[right]]=1
            while len(d)>k:
                d[s[left]]-=1
                if d[s[left]]==0:
                    del d[s[left]]
                left+=1
            if len(d)==k:
                length=max(length,right-left+1)
            right+=1
        return length