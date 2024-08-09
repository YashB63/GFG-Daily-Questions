class Solution:
    def countTriplets(self, n, sum_val, arr):
        arr.sort()
        
        count = 0
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                if arr[i] + arr[left] + arr[right] < sum_val:
                    count += (right - left)
                    left += 1
                else:
                    right -= 1
        
        return count