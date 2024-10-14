import math

class Solution:
    def damonPrime (self, N):
        for i in range(2,int(math.sqrt(N+1))+1):
            if (N+1)%i==0:
                return "No"
        for i in range(2,int(math.sqrt(N-1))+1):
            if (N-1)%i==0:
                return "No"
        return "Yes"