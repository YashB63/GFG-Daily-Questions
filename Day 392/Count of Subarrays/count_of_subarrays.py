class Solution:
    
	def countSubarray(self,arr, n, k):
        count = 0
        prev = -1
        for i in range(0,n):
            if arr[i] > k:
                count += n - i
                count += i - prev -1
                count += ( n - i - 1 )  * ( i - prev - 1 )
                prev = i
        return count