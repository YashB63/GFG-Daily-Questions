class Solution:
    def sequence(self, n):
        
        j = 1
        x = 0
        for i in range(1, n+1):
            y = 1
            k = i
            while k > 0:
                y = (y*j)%((10**9) + 7)
                k = k - 1
                j = j + 1
            x = (x + y)%((10**9) + 7)
        return x