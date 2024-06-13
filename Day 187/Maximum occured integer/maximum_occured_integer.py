class Solution:
    
    def maxOccured(self,n, l, r, maxx):
        
        freq = [0] * (maxx + 2)
        
        for i in range(n):
            freq[l[i]] += 1
            if r[i] + 1 <= maxx:
                freq[r[i] + 1] -= 1
        
        max_occurrence = freq[0]
        result = 0
        
        for i in range(1, maxx + 1):
            freq[i] += freq[i - 1]
            if freq[i] > max_occurrence:
                max_occurrence = freq[i]
                result = i
        
        return result