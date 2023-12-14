class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        if K > len(Arr):
            return -1
            
        max_sum = sum(Arr[:K])
        window_sum = max_sum
        
        for i in range(K, len(Arr)):
            window_sum += Arr[i] - Arr[i-K]
            max_sum = max(max_sum, window_sum)
            
        return max_sum