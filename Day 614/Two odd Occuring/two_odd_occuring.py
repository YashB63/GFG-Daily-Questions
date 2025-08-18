class Solution:
    def twoOddNum(self, arr):
        xor2 = arr[0]  
        n = len(arr)
        x = 0
        y = 0

        for i in range(1, n):
            xor2 ^= arr[i]

        set_bit_no = xor2 & ~(xor2 - 1)

        for i in range(n):
            if arr[i] & set_bit_no:
                x ^= arr[i]
            else:
                y ^= arr[i]

        if x > y:
            return [x, y]
        else:
            return [y, x]