class Solution:
    def divide(self, dividend, divisor):
        if dividend == divisor:
            return 1

        sign = (dividend > 0) == (divisor > 0)

        n = abs(dividend)
        d = abs(divisor)
        ans = 0

        while n >= d:
            cnt = 0
            while n >= (d * (1 << (cnt + 1))):
                cnt += 1
            ans += (1 << cnt)
            n -= d * (1 << cnt)

        if ans >= 2**31:
            return (2**31 - 1) if sign else -2**31

        return ans if sign else -ans