class Solution:
    def minSteps(self, str : str) -> int:
        prev=None;acount=0;bcount=0
        for i in str:
            if i==prev:
                continue
            if i=='a':
                acount+=1
            else:
                bcount+=1
            prev=i
        return min(acount,bcount)+1