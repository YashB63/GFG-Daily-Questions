class Solution:
    def search(self, n, arr):
        xor = 0 
        for i in range(n) :
           xor ^= arr[i]
        return xor