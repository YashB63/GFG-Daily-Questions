class Solution:
    def check_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
                
        return True
        
    def prime_sum(self, num):
        factors_sum = 0
        divisor = 2
        
        while num > 1:
            if num % divisor == 0:
                while num % divisor == 0:
                    num //= divisor
                    factors_sum += sum(int(digit) for digit in str(divisor))
            divisor += 1
        
        return factors_sum
        
    def smithNum(self, n):
        def sum_of_digits(num):
            return sum(int(digit) for digit in str(num))
        
        if self.check_prime(n):
            return 0
            
        digits_sum = sum_of_digits(n)
        factors_sum = self.prime_sum(n)
        
        return 1 if digits_sum == factors_sum else 0