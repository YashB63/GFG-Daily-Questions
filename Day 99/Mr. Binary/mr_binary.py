class Solution:
    def maximum_index(self, s):
       
        set1=set(s[0])
        ans=0
        for i in range(1, len(s)):
            if s[i] in set1 or chr(ord(s[i])-1) in set1:
                ans=i
                set1.add(s[i])
        return ans