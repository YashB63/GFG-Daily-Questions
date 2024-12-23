class Solution:
    
    def rotateMatrix(self,arr, n):
        for i in range(n):
            arr[i]=arr[i][::-1]
        for i in range(n):
            for j in range(i,n):
                if(i!=j):
                    arr[i][j], arr[j][i]=arr[j][i], arr[i][j]