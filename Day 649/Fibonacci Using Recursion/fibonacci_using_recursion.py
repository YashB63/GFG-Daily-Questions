class Solution:
    def nthFibonacci(self, n):
        if n <= 1:
            return n
        return self.nthFibonacci(n - 1) + self.nthFibonacci(n - 2)