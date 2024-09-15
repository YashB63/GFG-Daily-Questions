class Solution:
	def countPairsWithDiffK(self,arr, k):
        freq = {}
        count = 0

        for num in arr:
            if num - k in freq:
                count += freq[num - k]
            if num + k in freq:
                count += freq[num + k]
        
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        return count