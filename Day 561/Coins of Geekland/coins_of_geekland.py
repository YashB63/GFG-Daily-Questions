class Solution:
    def Maximum_Sum(self, mat, N, K):
        stripSum=[[0]*N for i in range(N)] 
        
        for j in range(N): 
            sum = 0 
            for i in range(K):
                sum += mat[i][j] 
            stripSum[0][j] = sum 
    
            for i in range(1,N-K+1):
                sum += (mat[i+K-1][j] - mat[i-1][j]) 
                stripSum[i][j] = sum
    
        max_sum =-10**9
    
        for i in range(N-K+1):
            sum = 0; 
            for j in range(K):
                sum += stripSum[i][j] 
            if (sum > max_sum):
                max_sum = sum 
    
            for j in range(1,N-K+1): 
                sum += (stripSum[i][j+K-1] - stripSum[i][j-1]) 
    
                if (sum > max_sum):
                    max_sum = sum 
        return max_sum