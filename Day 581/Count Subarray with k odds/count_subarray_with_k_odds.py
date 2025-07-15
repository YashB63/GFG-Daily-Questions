class Solution:
    def solve(self, n, nums, k):
        count = 0
        oddCount = 0
        left = 0
        right = 0

        while right < n:
            if nums[right] % 2 == 1:
                oddCount += 1

            while oddCount > k:
                if nums[left] % 2 == 1:
                    oddCount -= 1
                left += 1

            count += (right - left + 1)
            right += 1

        return count

    def countSubarray(self, n, nums, k):
        solution = Solution()
        return solution.solve(n, nums, k) - solution.solve(n, nums, k - 1)