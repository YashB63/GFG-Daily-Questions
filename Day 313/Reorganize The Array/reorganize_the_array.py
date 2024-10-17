import math

class Solution:
    def countFactors (self, N):
        count=0
        for i in range(1,int(math.sqrt(N))+1):
            if(N%i==0):
                if(i!=N//i):
                    count=count+2
                else:
                    count=count+1
        return count