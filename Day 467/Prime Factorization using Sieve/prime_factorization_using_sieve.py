from math import sqrt

class Solution:
    def sieve(self):
        N = 2*pow(10, 5)
        primes = [num for num in range(N+1)]
        primes[0] = primes[1] = -1
        
        lim = int(sqrt(N))+1
        for idx in range(2, lim):
            if primes[idx] != idx:
                continue
            
            for multIdx in range(idx*idx, N+1, idx):
                if primes[multIdx] == multIdx:
                    primes[multIdx] = idx
                    
        self.primes = primes
        
    def findPrimeFactors(self, N):
        primes = self.primes
        ans = []
        while N > 1:
            ans.append(primes[N])
            N //= primes[N]
            
        return ans