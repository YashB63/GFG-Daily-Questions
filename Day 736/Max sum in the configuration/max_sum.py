class Solution:
    def maxSum(self, arr): 
        n = len(arr)
        
        arrSum = sum(arr)
        currVal = 0
        for i in range(n):
            currVal += i * arr[i]
            
        maxVal = currVal
        
        for i in range(1, n):
            currVal = currVal + arrSum - n * arr[n - i]
            maxVal = max(maxVal, currVal)

        return maxVal