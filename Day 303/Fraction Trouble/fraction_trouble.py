import math as mt

class Solution:
	def numAndDen(self, n, d):
        num=-1
        den=1
        f=d+1
        for i in range (f,10001):
            x=(n*i)//d
            if mt.gcd(x,i)==1:
                if (1.0*x/i>1.0*num/den):
                    num=x
                    den=i
        return (num,den)