class Solution:
    def count(self, n):
        total_combination = (n*(n-1))/2
        return int(2**total_combination)