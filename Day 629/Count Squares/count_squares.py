class Solution:
    def countSquares(self, N):
        if N==1:
            return 0
        low, high = 1, N
        result = 0

        while low <= high:
            mid = (low + high) // 2
            if mid * mid == N:
                return mid - 1
            elif mid * mid < N:
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        return result