class Solution:
    def isPossible(self, maxTime, arr, k):
        painters = 1
        currSum = 0

        for length in arr:
            if length > maxTime:
                return False

            if currSum + length > maxTime:
                painters += 1
                currSum = length
            
            else:
                currSum += length

        return painters <= k

    def minTime(self, arr, k):
        low = max(arr)
        high = sum(arr)
        result = high

        while low <= high:
            mid = (low + high) // 2

            if self.isPossible(mid, arr, k):
                result = mid
                high = mid - 1
    
            else:
                low = mid + 1

        return result