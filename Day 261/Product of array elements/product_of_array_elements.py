class Solution:
    def product(self, arr):
        product=1
        for i in arr:
            product*=i
            
        if product>=1000000007:
            product%=1000000007
        return product