class Solution:
	def AllPrimeFactors(self, N):
        prime_factors = []
        
        if N % 2 == 0:
            prime_factors.append(2)
            while N % 2 == 0:
                N //= 2
        
        for i in range(3, int(N ** 0.5) + 1, 2):
            if N % i == 0:
                prime_factors.append(i)
                while N % i == 0:
                    N //= i
        
        if N > 2:
            prime_factors.append(N)
        
        return prime_factors