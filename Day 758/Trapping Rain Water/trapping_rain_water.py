class Solution:
    def maxWater(self, arr):
        n = len(arr)
        if n < 3:
            return 0
    
        l, r = 0, n - 1
        leftMax = rightMax = 0
        water = 0
    
        while l <= r:
            if arr[l] <= arr[r]:
                if arr[l] >= leftMax:
                    leftMax = arr[l]
                else:
                    water += leftMax - arr[l]
                l += 1
            else:
                if arr[r] >= rightMax:
                    rightMax = arr[r]
                else:
                    water += rightMax - arr[r]
                r -= 1
    
        return water