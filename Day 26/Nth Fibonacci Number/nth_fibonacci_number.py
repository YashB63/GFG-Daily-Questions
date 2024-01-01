class Solution:
    def nthFibonacci(self, n : int) -> int:
        
        mod = 1000000007
        
        arr = [0]*(n+1)
        arr[0] = 0
        arr[1] = 1
        
        for i in range(2, n+1):
            arr[i] = (arr[i-1] + arr[i-2]) % mod
        return arr[n]