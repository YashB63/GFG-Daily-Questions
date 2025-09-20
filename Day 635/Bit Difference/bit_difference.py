class Solution:
    def countSetBits(self, n):
        count = 0
        
        while (n > 0):
            count += n & 1
            n >>= 1
        return count

    def countBitsFlip(self, a, b):
        ans = 0
        ans = a ^ b
        return self.countSetBits(ans)