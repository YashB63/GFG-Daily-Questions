from collections import Counter

class Solution:
    
    def winner(self,arr,n):
        
        return sorted(Counter(arr).items(), key=lambda x:(-x[1],x[0]))[0]
