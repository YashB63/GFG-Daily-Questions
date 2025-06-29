class Solution:
    def countSub(self, arr):
        MOD = 10**9 + 7

        count = [0] * 10

        for i in range(len(arr)):
            for j in range(arr[i] - 1, -1, -1):
                count[arr[i]] = (count[arr[i]] + count[j]) % MOD

            count[arr[i]] = (count[arr[i]] + 1) % MOD

        result = sum(count) % MOD

        return result