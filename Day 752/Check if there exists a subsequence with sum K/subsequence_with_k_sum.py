class Solution:
    def checkSubsequenceSum(self, N, arr, K):
        target = K
        size = N
        total = 0  

        def helper(i):
            nonlocal total

            if total > target:
                return False
            if total == target:
                return True
            if i >= size:
                return False

            res1 = helper(i + 1)
            if res1:
                return True

            total += arr[i]
            res2 = helper(i + 1)
            total -= arr[i]

            if res2:
                return True

            return False

        return helper(0)