class Solution:
    def numoffbt(self, arr, n):
        maxi = max(arr)
        mini = min(arr)
        dp = [0] * (maxi+1)

        for i in arr:
            dp[i] = 1
        output = 0

        for i in range(mini,maxi+1):
            if dp[i] != 0:
                j = i+i
                while j<=maxi and (j/i)<=i:
                    if dp[j] != 0:
                        dp[j] += (dp[i] * dp[j//i])
                        if i!=j/i:
                            dp[j] += (dp[i]*dp[j//i])
                    j += i

                output += dp[i]
                output %= 1000000007

        return output