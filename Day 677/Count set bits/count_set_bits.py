class Solution:
    def countSetBits(self, n):
        if n == 0:
            return 0

        x = int(math.log2(n))

        if x == 0:
            return 1  

        fullBits = x * (1 << (x - 1))

        msbBits = n - (1 << x) + 1

        remaining = n - (1 << x)
        remainingBits = self.countSetBits(remaining)

        return fullBits + msbBits + remainingBits