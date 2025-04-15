class Solution:
    def comb(self, n, k):
        if k > n:
            return 0
        num = 1
        denom = 1
        for i in range(k):
            num *= n - i
            denom *= i + 1
        return num // denom
        
    def findgroups(self, arr):
        mod = [0] * 3
        for num in arr:
            mod[num % 3] += 1
        
        pairs = self.comb(mod[0], 2) + mod[1] * mod[2]
        triplets = (self.comb(mod[0], 3) + self.comb(mod[1], 3) + 
                    self.comb(mod[2], 3) + mod[0] * mod[1] * mod[2])
        
        res = pairs + triplets
        return res