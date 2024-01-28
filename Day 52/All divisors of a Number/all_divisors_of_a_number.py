import math

class Solution:
    def print_divisors(self, N):
        
        x = []
        for i in range(1, math.floor(math.sqrt(N)) + 1):
            if N%i == 0:
                if N//i != i:
                    x.append(i)
                    x.append(N//i)
                else:
                    x.append(i)
        
        for i in sorted(x):
            print(i, end= " ")