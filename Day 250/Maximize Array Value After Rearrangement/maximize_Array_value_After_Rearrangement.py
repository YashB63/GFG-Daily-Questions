class Solution:
    def Maximize(self, arr): 
        MOD = 10**9 + 7
    
        arr.sort()
        
        max_sum = 0
        for i in range(len(arr)):
            max_sum = (max_sum + arr[i] * i) % MOD
    
        return max_sum