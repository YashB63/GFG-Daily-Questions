class Solution:
    def swapBits(self,n):
        odd_mask = 0xAAAAAAAA
        even_mask = 0x55555555
        
        oddset = n & odd_mask
        evenset = n & even_mask
        
        odd_shifted = oddset >> 1
        even_shifted = evenset << 1
        return odd_shifted | even_shifted