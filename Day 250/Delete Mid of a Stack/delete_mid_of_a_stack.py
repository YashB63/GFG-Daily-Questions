class Solution:
    def deleteMid(self, s, sizeOfStack):
        n = len(s)
        if n%2!=0:
            s.pop(n//2)
        else:
            s.pop(n//2-1)