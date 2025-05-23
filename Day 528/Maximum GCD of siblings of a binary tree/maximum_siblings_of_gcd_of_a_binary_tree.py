class Solution:
    def maxBinTreeGCD(self, arr, N):
        if (len(arr) == 1 or len(arr) == 0):
            return 0
      
        arr.sort()

        a = arr[0]
        ans = 0
        for i in range(1, len(arr)):
            b = arr[i]

            if (b[0] == a[0]):
                ans = max(ans, gcd(a[1], b[1]))

            a = b
        return ans