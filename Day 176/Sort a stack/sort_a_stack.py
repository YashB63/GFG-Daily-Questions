class Solution:
    
    def Sorted(self, s):
        
        lst=[]
        while s:
            lst.append(s.pop())
        lst.sort()
        for i in lst:
            s.append(i)