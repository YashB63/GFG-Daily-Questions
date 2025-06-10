class Solution:
    def maxModValue(self, arr):
        n = len(arr)
        ans = 0

        arr.sort()

        for j in range(n - 2, -1, -1):
            if ans >= arr[
                    j]:  
                break
            if arr[j] == arr[
                    j +
                    1]:  
                continue

            for i in range(2 * arr[j], arr[n - 1] + arr[j] + 1, arr[j]):
                ind = self.lower_bound(arr, i)
                if ind > 0:  
                    ans = max(ans, arr[ind - 1] % arr[j])

        return ans 

    def lower_bound(self, arr, x):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        return left