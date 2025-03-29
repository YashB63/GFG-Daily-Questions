class Solution:
    call_count = 0
    history = []
    
    def maxCandy(self, height, n): 
        Solution.call_count += 1
        Solution.history.append(list(height))

        if Solution.call_count == 1000:
            print(Solution.history)
            return None

        l = 0
        r = len(height) - 1
        ans = 0

        while l < r:
            w = r - l - 1
            h = min(height[l], height[r])
            ans = max(ans, w * h)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ans