class Solution:
    def findWinner(self, n, A):
       
        x = 0
        
        for i in range(n):
            x ^= A[i]
        if(x == 0 or n%2 == 0):
            return 1
        else:
            return 2