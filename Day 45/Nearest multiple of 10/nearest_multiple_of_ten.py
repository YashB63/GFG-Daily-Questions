class Solution:
    def roundToNearest (self, N) : 
        
        n = int(N)
        rem = n%10
        
        if rem <= 5:
            x = n - rem
        else:
            x = n + (10-rem)
        
        return str(x)