class Solution:
    
    def maxSubArraySum(self,arr,N):
       
        x = 0
        y = arr[0]
        for i in arr:
            x += i
            y = max(x, y)
            if x < 0:
                x = 0
        return y