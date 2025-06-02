class Solution:
    def sumOfDigits(self, n):
        if n<10: 
            return n
    
        return (n%10) + (self.sumOfDigits(n//10))
    
    def digitalRoot(self, n):
        sum_of_digits = self.sumOfDigits(n) 

        if sum_of_digits <10: 
            return sum_of_digits
        
        return self.digitalRoot(sum_of_digits)