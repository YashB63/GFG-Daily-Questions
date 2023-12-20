class Solution:
    def minValue(self, a, b, n):
        
        a.sort()
        b.sort(reverse=True)
        
        min_sum = 0
        for i in range(n):
            min_sum += a[i] * b[i]
            
        return min_sum
