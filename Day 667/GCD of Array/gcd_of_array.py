class Solution:
    def Gcd(self, a, b):
        if a > b:
            if a % b == 0:
                return b
            return self.Gcd(b, a % b)
        if b % a == 0:
            return a
        return self.Gcd(a, b % a)

    def gcd(self, n, arr):
        result = arr[0]

        for i in range(1, n):
            result = self.Gcd(result, arr[i])

        return result