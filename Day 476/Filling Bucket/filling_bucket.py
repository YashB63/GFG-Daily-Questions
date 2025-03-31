class Solution:
    def fillingBucket(self, N):
        a=1
        b=1
        for i in range(2, N+1):
            c=(a+b)%100000000
            a=b
            b=c
        return b