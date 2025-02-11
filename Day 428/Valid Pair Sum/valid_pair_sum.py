class Solution:
    def ValidPair(self, a, n): 
        a.sort()

        count = 0
        l = 0
        r = n - 1
    
        while l < r:
            if a[l] + a[r] >= 1:
                count += r - l
                r -= 1
            else:
                l += 1
    
        return count