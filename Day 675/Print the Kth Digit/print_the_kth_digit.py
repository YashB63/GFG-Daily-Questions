class Solution:
    def kthDigit(self, a, b, k):
        x = pow(a, b)
        temp = 0
        
        while (k > 0):
            temp = x % 10
            x = x // 10
            k -= 1
            
        return temp