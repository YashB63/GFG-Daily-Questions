class Solution:
    def sumOfDivisors(self, N):
        sum=0
        for i in range(1,N+1):
            sum=sum+(N//i)*i
        return sum