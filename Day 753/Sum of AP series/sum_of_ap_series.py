class Solution:
    def sum_of_ap(self, n, a, d):
        total_sum = (n * (2*a + (n-1)*d))//2
        
        return total_sum