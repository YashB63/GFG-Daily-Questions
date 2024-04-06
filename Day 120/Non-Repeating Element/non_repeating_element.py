class Solution:
    def firstNonRepeating(self, arr, n): 
        
        for i in arr:
            if arr.count(i)==1:
                
                return i
        return 0