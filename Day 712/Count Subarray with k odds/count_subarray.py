class Solution:
    def atMostX(self, arr, x):
        n = len(arr)
        odd = 0
        ans = 0
        start = 0

        for i in range(n):
            if arr[i] % 2 != 0:
                odd += 1

            while odd > x:
                if arr[start] % 2 != 0:
                    odd -= 1
                start += 1

            ans += i - start + 1

        return ans

    def countSubarrays(self, arr, k):
        n = len(arr)
        x = self.atMostX(arr, k)
        y = self.atMostX(arr, k - 1)

        return x - y