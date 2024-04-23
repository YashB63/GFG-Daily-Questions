class Solution:
    def sieveOfEratosthenes(self, N):
    	
        primes =[]
        Q= [True] *(N+1) # is prime
        for i in range(2, N + 1):
            if Q[i]:
                primes.append(i)
                for j in range(i * i, N + 1, i):
                    Q[j] = False
        return primes