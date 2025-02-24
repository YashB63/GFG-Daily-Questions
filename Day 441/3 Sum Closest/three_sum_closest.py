class Solution:
    def closest3Sum(self, arr, target):
        n = len(arr)
        arr.sort() 
        res = 0
        minDiff = float('inf')

        for i in range(n - 2):
            
         l, r = i + 1, n - 1

         while l < r:
            currSum = arr[i] + arr[l] + arr[r]
            
            if abs(currSum - target) < minDiff:
                minDiff = abs(currSum - target)
                res = currSum
    
            elif abs(currSum - target) == minDiff:
                res = max(res, currSum)

            if currSum > target:
                r -= 1

            else:
                l += 1

        return res