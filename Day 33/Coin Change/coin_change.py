class Solution:
    def count(self, coins, N, Sum):
        
        X = [0] * (Sum + 1)
        X[0] = 1
        
        for i in coins:
            for j in range(i, Sum + 1):
                X[j] += X[j-i]
        return X[Sum]