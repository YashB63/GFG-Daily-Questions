class Solution:    
    def countX(self,L,R,X):
        count = 0
        for i in range(L+1, R):
            count += str(i).count(str(X))
        return count