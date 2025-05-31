class Solution:
    MOD = int(1e9 + 7)

    def __init__(self):
        self.fac = []  

    def power(self, x, y, p):
        res = 1
        x = x % p

        while y > 0:
            if y & 1: 
                res = (res * x) % p
            y >>= 1  
            x = (x * x) % p  
        return res % p

    def modInverse(self, n, p):
        return self.power(n, p - 2, p)

    def nCrModPFermat(self, n, r, p):
        if r == 0:
            return 1
        if n < r:  
            return 0
        return (self.fac[n] * self.modInverse(self.fac[r], p) % p *
                self.modInverse(self.fac[n - r], p) % p) % p

    def factorial(self, n):
        self.fac = [0] * (n + 1)  
        self.fac[0] = 1
        for i in range(1, n + 1):
            self.fac[i] = (self.fac[i - 1] * i) % self.MOD

    def getAnswer(self, arr, k, x):
        n = len(arr)
        self.factorial(n)  
        arr.sort()  
        ans = 0
        i, j = 0, 0

        while j < n:
            while j < n and arr[j] - arr[i] <= x:
                j += 1
            if (j - i) >= k:  
                ans = (ans + self.nCrModPFermat(j - i - 1, k - 1, self.MOD)
                       ) % self.MOD  
            i += 1
        return ans