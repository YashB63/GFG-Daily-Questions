class Solution:
    def maxSubArraySum(self,arr):
        maxSoFar = -10000000
        maxEndingHere = 0
        for i in arr:
            maxEndingHere += i
            if(maxSoFar < maxEndingHere):
                maxSoFar = maxEndingHere
            if(maxEndingHere < 0):
                maxEndingHere = 0
        return maxSoFar