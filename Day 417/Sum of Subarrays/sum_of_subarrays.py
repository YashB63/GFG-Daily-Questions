class Solution:
    def subarraySum(self, arr):
        n = len(arr)
        ans = 0
        for i in range(n): 
            a = i + 1
            b = n - i
            ans += arr[i] * (a) * (b)
        return ans % ((10 ** 9) + 7)