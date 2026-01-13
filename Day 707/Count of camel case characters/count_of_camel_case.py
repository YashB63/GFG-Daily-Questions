class Solution:
    def countCamelCase (self,s):
        ct=0
        for i in s:
            if i.isupper():
                ct=ct+1
        return ct