N=10**4
prime = [True]*N
i=2
while i*i<N:
    if prime[i]:
        for j in range(i*i, N, i):
            prime[j] = False
            
    i+=1
prime[0]=False
prime[1]=False

class Solution:
	def sixyPrime(self, L, R):
        ans = []
        for i in range(L, R+1):
            if prime[i]:
                if prime[i+6] and (i+6)<=R:
                    ans.append(i)
                    ans.append(i+6)
        
        if not ans:
            return [-1]
        return ans