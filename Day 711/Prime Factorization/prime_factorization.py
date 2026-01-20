class Solution:
    def isPrime(self, n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def printPrimeFactorization(self, n):
        for i in range(2, n + 1):
            if self.isPrime(i):
                x = i
                while n % x == 0:
                    print(i, end=" ")
                    x *= i