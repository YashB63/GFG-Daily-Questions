class Solution:
    def subarrayXor(self, arr, k):
        memo = {0: 1} 
        
        current_xor = 0
        total_subarrays = 0
        
        for num in arr:
            current_xor ^= num
            target = current_xor ^ k
            if target in memo:
                total_subarrays += memo[target]
            if current_xor in memo:
                memo[current_xor] += 1
            else:
                memo[current_xor] = 1
                
        return total_subarrays