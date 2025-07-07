class Solution:
    def findDivisors(self, n):
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                if n // i == i:
                    divisors.append(i)
                else:
                    divisors.append(i)
                    divisors.append(n // i)
        return divisors

    def printPairs(self, arr, k):
        n = len(arr)
        ans = 0
        occ = {}

        for num in arr:
            occ[num] = True

        isPairFound = False

        for num in arr:
            if k in occ and k < num:
                ans += 1
                isPairFound = True

            if num >= k:
                divisors = self.findDivisors(num - k)
                for divisor in divisors:
                    if num % divisor == k and num != divisor and divisor in occ:
                        ans += 1
                        isPairFound = True

        return ans