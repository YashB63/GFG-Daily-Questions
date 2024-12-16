class Solution:
    def closestToZero (self,arr, n):
        arr.sort()
        left, right = 0, len(arr) - 1
        closest_sum = float('inf')
        
        while left < right:
            current_sum = arr[left] + arr[right]
            if abs(current_sum) < abs(closest_sum):
                closest_sum = current_sum
            elif abs(current_sum) == abs(closest_sum) and current_sum > closest_sum:
                closest_sum = current_sum
            if current_sum > 0:
                right -= 1
            else:
                left += 1
        
        return closest_sum