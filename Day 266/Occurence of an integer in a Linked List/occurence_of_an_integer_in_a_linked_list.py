class Solution:
	def prime_Sum(self, n):
        prime=[True]*(n+1)
        p=2
        while p*p<=n:
            if prime[p]:
                for i in range(p*p,n+1,p):
                    prime[i]=False
            p+=1
        s=0
        for i in range(2,n+1):
            if prime[i]:
                s+=i
        return s