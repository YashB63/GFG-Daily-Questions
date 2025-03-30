class Solution:
    def killinSpree (self, n):
        left, right = 1, int(n ** 0.5)  
        result = 0  
    
        while left <= right:
            mid = (left + right) // 2  
            sum_squares = (mid * (mid + 1) * (2 * mid + 1)) // 6  
            
            if sum_squares <= n:  
                result = mid  
                left = mid + 1  
            else:
                right = mid - 1 
    
        return result