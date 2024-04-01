class Solution:
    def evenlyDivides (self, N):
        
        count=0
        value=N
        while N!=0:
            n=N%10
            if (n!=0) and ((value % n) == 0):
                count = count+1
            N=N//10
        return count