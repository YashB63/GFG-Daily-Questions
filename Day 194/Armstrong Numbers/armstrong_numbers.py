class Solution:
    def armstrongNumber (self, n):
        # code here 
        sum_of_cubes = 0
        original = n
    
        while n > 0:
            digit = n % 10  
            sum_of_cubes += digit ** 3  
            n //= 10  
    
        if sum_of_cubes==original:
            return "true"
        return "false"