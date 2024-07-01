class Solution:
    def findTwoElement( self,arr, n): 
        
        A,B = 0,0
        
        for i in arr:
            if arr[abs(i)-1] < 0:
                A = abs(i)
            else:
                arr[abs(i)-1] *= -1
                
        for i in range(n):
            if arr[i] > 0:
                B = i+1
                break
            
        return [A,B]