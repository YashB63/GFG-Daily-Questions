N=10**6
prime = [True]*N
i=2
while i*i<N:
    if prime[i]:
        for j in range(i*i, N, i):
            prime[j] = False
            
    i+=1
    
class Solution:
    def nthMysterious (self, N):
        for i in range(2, 10**6):
            if prime[i]:
                N-=1
            if N==0:
                break
            
        return i*i+1