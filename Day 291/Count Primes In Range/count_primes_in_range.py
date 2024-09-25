class Solution:
    def sieve(self, L, R):
        n=(2*10**5)+1
        prime = [1]*n
        prime[0], prime[1] = 0,0
        for i in range(2, int(n**0.5)+1):
            if prime[i]:
                for j in range(i*i, n,i):
                    prime[j]=0 
        cnt = 0
        for i in range(2, n):
            cnt+=prime[i]
            prime[i]=cnt
        return prime
    
    def countPrimes(self,L,R):
        prime=Solution.sieve(self, L, R)
        return prime[R]-prime[L-1]