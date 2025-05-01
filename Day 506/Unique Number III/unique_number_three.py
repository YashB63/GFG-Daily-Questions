class Solution:
    def getSingle(self, arr):
        ones, twos = 0, 0
        for number in arr:
            twos |= ones & number
            ones ^= number
            common_bits = ones & twos
            ones &= ~common_bits
            twos &= ~common_bits
        
        return ones