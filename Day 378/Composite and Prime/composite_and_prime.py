class Solution:
	def sieve(self, l, r):
        count = 0
        prime = [True for i in range(R+1)]
        p = 2
        while (p * p <= R):
            if (prime[p] == True):
                for i in range(p * p, R+1, p):
                    prime[i] = False
            p += 1
    
        for p in range(L, R+1):
            if prime[p]:
                count += 1
        return count
        
    def Count(self, L, R):
        
        primes = self.sieve(L,R)
        
        if L == 1:
            primes = primes - 1
        
        composites = R - L + 1 - primes
        return composites - primes if L > 1 else composites - primes - 1