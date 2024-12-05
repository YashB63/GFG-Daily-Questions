class Solution:
    def count (self, N):
        count = 0
        
        for i in range(1,N + 1):
            if '3' not in str(i):
                count += 1
                
        return count