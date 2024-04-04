class Solution:
    def josephus(self,n,k):
        
        if n == 1:
            return 1
        temp = (Solution().josephus(n-1,k)) + k
        if temp % n == 0:
            return n
        else:
            return temp % n