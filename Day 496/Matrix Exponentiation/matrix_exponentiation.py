class Solution:
	def FindNthTerm(self, n):
        if n == 0 or n == 1:
            return 1
            
        n -= 1
        matrix = [[1, 1], [1, 0]]
        res = [[1, 1], [1, 0]]
        MOD = 10**9+7
        
        while n > 0:
            if n & 1:
                r_1 = (matrix[0][0] * res[0][0] + matrix[0][1] * res[1][0]) % MOD
                r_2 = (matrix[0][0] * res[0][1] + matrix[0][1] * res[1][1]) % MOD
                r_3 = (matrix[1][0] * res[0][0] + matrix[1][1] * res[1][0]) % MOD
                r_4 = (matrix[1][0] * res[0][1] + matrix[1][1] * res[1][1]) % MOD
                res = [[r_1, r_2], [r_3, r_4]]
            val_1 = (matrix[0][0] * matrix[0][0] + matrix[0][1] * matrix[1][0]) % MOD
            val_2 = (matrix[0][0] * matrix[0][1] + matrix[0][1] * matrix[1][1]) % MOD
            val_3 = (matrix[1][0] * matrix[0][0] + matrix[1][1] * matrix[1][0]) % MOD
            val_4 = (matrix[1][0] * matrix[0][1] + matrix[1][1] * matrix[1][1]) % MOD
            matrix = [[val_1, val_2], [val_3, val_4]]
            n >>= 1
        
        return res[0][0]