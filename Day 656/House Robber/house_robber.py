class Solution:
    def maximizeMoney(self, N , K):
        if N%2==1:
            ans = ((N//2)+1)*K        
        else:
            ans = (N//2)*K            
        
        return ans