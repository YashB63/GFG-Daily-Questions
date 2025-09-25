class Solution:
    def checkYear(self, N):
        if (N % 100 == 0):
            if (N % 400 == 0):
                return True
            else:
                return False
        
        elif (N % 4 == 0):
            return True
        else:
            return False