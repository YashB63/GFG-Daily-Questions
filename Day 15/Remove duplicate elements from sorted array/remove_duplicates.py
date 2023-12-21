class Solution:	
	def remove_duplicate(self, A, N):
		
        if N == 0 or N == 1:
            return N
            
        count = 0
        
        for i in range(N - 1):
            if A[i] != A[i+1]:
                A[count] = A[i]
                count += 1
                
        A[count] = A[N - 1]
        count += 1
        
        return count