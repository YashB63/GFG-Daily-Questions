class Solution:
    
    def rotateby90(self,a, n): 
        
        for i in range(n):
            for j in range(n//2):
                a[i][j] , a[i][n-j-1] = a[i][n-j-1],a[i][j]
                
        for i in range(n):
            for j in range(i+1,n):
                a[i][j] , a[j][i] = a[j][i],a[i][j]