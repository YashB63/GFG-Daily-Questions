class Solution:
    def minimumEnergy(self, height, n):
        
        prev = 0
        prev2 = 0
        for i in range(1, n):
            oneStep = prev + abs(height[i] - height[i-1])
            twoStep = float('inf')
            if i > 1:
                twoStep = prev2 + abs(height[i] - height[i-2])
            curri = min(oneStep, twoStep)
            prev2 = prev
            prev = curri
        return prev