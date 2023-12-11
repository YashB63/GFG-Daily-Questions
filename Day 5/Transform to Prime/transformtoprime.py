def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    
    return True


class Solution:
    def minNumber(self, arr,n):
        total_sum = sum(arr)
        
        if check_prime(total_sum):
            return 0
            
        for i in range(1, total_sum + 1):
            if check_prime(total_sum + i):
                return i