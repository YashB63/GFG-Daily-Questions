from collections import Counter
class Solution:
    def check(self,A,B,N):
        
        count_a = Counter(A)
        count_b = Counter(B)
        
        return count_a == count_b