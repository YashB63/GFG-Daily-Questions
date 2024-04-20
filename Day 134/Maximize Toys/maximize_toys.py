class Solution:
    def toyCount(self, N, K, arr):
        
        arr.sort()
        count=0
        for i  in range(0,N):
            if K<arr[i]:
                return count
            else:
                K=K-arr[i]
                count+=1
        
        return count