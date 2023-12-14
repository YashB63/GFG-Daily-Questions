class Solution:
    def getPairsCount(self, arr, n, k):
        freq = {}
        count = 0
        
        for num in arr:
            if k - num in freq:
                count += freq[k - num]
                
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
                
        return count