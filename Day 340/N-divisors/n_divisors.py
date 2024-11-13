import math

class Solution:
    def count(self,A,B,N): 
        def count_divisors(x):
            divisor_count = 0
            for i in range(1, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    if i * i == x:
                        divisor_count += 1
                    else:
                        divisor_count += 2
            return divisor_count
        
        count = 0
        
        for x in range(A, B + 1):
            if count_divisors(x) == N:
                count += 1
        
        return count