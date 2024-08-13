class Solution:
    def Maximize(self, arr): 
        MOD = 10**9 + 7
        
        arr.sort()
        
        result = 0
        
        for i in range(len(arr)):
            result = (result + arr[i] * i) % MOD
        
        return result