class Solution:
    def isPrime(self,x):
        if x==1:
            return False
        i=2
        while i*i<=x:
            if x%i==0:
                return False
            i+=1
        return True
        
	def minThirdPiles(self, A, B):
        k=1
        while True:
            sum=A+B+k
            if self.isPrime(sum) or sum==1:
                return k
            k+=1