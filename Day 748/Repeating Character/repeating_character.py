class Solution:
    def repeatingCharacter(self,s):
        c=0
        for i in s:
            if s.count(i) > 1:
                return c
            c+=1
        return -1