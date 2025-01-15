class Solution:
    def matchGame(self, A):
        if A < 0:
            return -1  

        if A % 5 == 0:
            return -1  
    
        return A % 5