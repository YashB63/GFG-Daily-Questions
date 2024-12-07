class Solution:
    
    def searchMatrix(self,mat, x): 
    	n=len(mat)
        m=len(mat[0])
        
        low=0
        high=n*m-1
        while low<=high:
            mid=(low+high)//2
            row=mid//m
            col=mid%m
            if mat[row][col]==x:
                return True
            elif mat[row][col]>x:
                high=mid-1
            else:
                low=mid+1
                
        return False