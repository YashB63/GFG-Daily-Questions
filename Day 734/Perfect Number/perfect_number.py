from math import factorial

class Solution:
    def isPerfect(self, N):
        temp = N
        factorial_sum = 0
        
        while(temp > 0):
            factorial_sum += factorial(temp % 10)
            temp = temp//10
        
        if(N == factorial_sum):
            return 1
        else:
            return 0