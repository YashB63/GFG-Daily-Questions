class Solution:
    def noOfDigits(self, N):
        if N < 2:
            return 1
        
        f1 = 0
        f2 = 1
        
        for _ in range(2, N+1):
            f1, f2 = f2, f1+f2
        return len(str(f2))