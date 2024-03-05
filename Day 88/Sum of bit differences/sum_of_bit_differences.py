class Solution:

	def sumBitDifferences(self,arr, n):
    	
        res = 0
        for i in range(31, -1, -1):
            one = 0
            zero = 0
            for j in range(n):
                bit = 1 << i
                if (arr[j] & bit) > 0:
                    one += 1
                else:
                    zero += 1
            res += (one * zero) * 2
        return res