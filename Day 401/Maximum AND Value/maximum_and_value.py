class Solution:
    def checkBit(self, pattern, arr,  n):
        count = 0
     
        for i in range(0, n):
            if ((pattern & arr[i]) == pattern):
                count = count + 1
        return count
        
    def maxAND(self, arr,N):
        res = 0
        for bit in range(31, -1, -1):
            count = self.checkBit(res | (1 << bit), arr, N)

            if (count >= 2):
                res = res | (1 << bit)
     
        return res