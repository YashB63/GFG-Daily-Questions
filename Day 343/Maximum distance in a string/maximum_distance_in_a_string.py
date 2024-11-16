class Solution:
    def maximum_distance(self, s):
        ans=0
        set1=set()

        if 'a' in s:
            ind=s.find('a')
            set1.add('a')
            ans=ind

        else:
            return -1

        for i in range (ind,len(s)):
            if (s[i] in set1 or chr(ord(s[i])-1) in set1) and s[i]!='a':
                set1. add(s[i])
                ans=i

        if len(set1)==1:
            return -1
        return ans+1