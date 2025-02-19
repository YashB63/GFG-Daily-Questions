class Solution:
	def superPrimes(self, n):
        if n < 5:
            return 0  
        
        is_prime = [True] * (n + 1)
        is_prime[0], is_prime[1] = False, False  
        
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        
        count = 0
        for i in range(5, n + 1):  
            if is_prime[i] and is_prime[i - 2]:
                count += 1
        
        return count