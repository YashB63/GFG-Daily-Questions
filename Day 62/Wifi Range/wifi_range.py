class Solution:
    def wifiRange(self, N, S, X): 
        
        y = 0
        for i in S:
            if(i=='1'):
                y = X
            else:
                y -= 1
                if(y < -X):
                    return False
                    
        if(y<0):
            return False
        return True