class Solution:
    def countPairs(self,arr, target):
        count = 0
        freq = {}
        
        for num in arr:
            complement = target - num
            if complement in freq:
                count += freq[complement]
            
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        return count