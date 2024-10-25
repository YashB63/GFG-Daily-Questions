class Solution:
    
    def isprime(self,N):
        i=2
        c=0
        while N!=1:
            d=0
            while N%i==0:
                N=N//i 
                d+=1
            c+=d
            if c>3 or d>1:
                return 0
            i+=1
        return c
        
	def isSphenicNo(self, N):
        return 1 if self.isprime(N)==3 else 0