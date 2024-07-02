
class Solution:
    #Function to find the days of buying and selling stock for max profit.
	def stockBuySell(self, A, n):
		
        if n < 2:
            return []
    
        result = []
        i = 0
    
        while i < n - 1:
            # Find local minimum
            while i < n - 1 and A[i + 1] <= A[i]:
                i += 1
        
            if i == n - 1:
                break
        
            buy = i
            i += 1
        
            # Find local maximum
            while i < n and A[i] >= A[i - 1]:
                i += 1
        
            sell = i - 1
        
            result.append([buy, sell])
    
        return result