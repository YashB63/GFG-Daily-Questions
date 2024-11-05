class Solution:
	def countPairsWithDiffK(self,arr, k):
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        pair_count = 0
    
        for num in freq:
            if (num + k) in freq:
                pair_count += freq[num] * freq[num + k]
    
        return pair_count