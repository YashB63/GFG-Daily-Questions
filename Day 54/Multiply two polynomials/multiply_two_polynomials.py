class Solution:
	def polyMultiply(self, Arr1, Arr2, M, N):
		
        x = [0] * (M+N-1)
        for i in range(0, M):
            f = 0
            for j in range(0, N):
                x[i + f] = x[i + f] + Arr1[i]*Arr2[j]
                f += 1
        return x